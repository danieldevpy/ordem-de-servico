import json
from typing import List
from src.application.infra.pyside.ui.core import QTableWidgetItem, Qt, QToolTip, QFont, QThread, QObject, Signal
from src.application.infra.pyside.page.main_window import Ui_MainWindow
from src.application.infra.sqlite.crud_order import get_orders
from src.application.infra.pyside.page.pdf_page import PDFPage
from src.domain.entity.order import Order
import time



class HistoryPage:

    def __init__(self, main_page: Ui_MainWindow) -> None:
        self.page = main_page
        self.orders: List[Order] = None
        self.filter_orders: List[Order] = None
        self.filter_fields = {}

    def assemble(self, search=None):
        self.page.stackedWidget.setCurrentIndex(3)
        self.page.radio_all.clicked.connect(lambda: self._set_filter(None))
        self.page.radio_open.clicked.connect(lambda: self._set_filter(1))
        self.page.radio_close.clicked.connect(lambda: self._set_filter(2))
        self.page.table_history_order.itemEntered.connect(self._change_cursor)
        self.page.table_history_order.itemDoubleClicked.connect(self._item_clicked)
        # self.page.lineEdit_search.textChanged.connect(self._search_line)
        self.page.btn_s_h_o.clicked.connect(self._search_orders)
        self._get_orders()
        self._set_filter_fields()

        
    def disassemble(self):
        self.orders = None
        self.filter_orders = None
        self.page.table_history_order.itemEntered.disconnect(self._change_cursor)
        self.page.table_history_order.itemDoubleClicked.disconnect(self._item_clicked)
        self.page.comboBox_search.clear()
        self._remove_orders()
        self._remove_filter()

    def _remove_order_list(self, order: Order):
        self.orders.remove(order)
        self.filter_orders.remove(order)

    def _get_orders(self):
        self.orders = get_orders()

    def _set_value_progressBar(self, value: int):
        self.page.progressBar.setValue(value)

    def _set_value_comboBox(self, fields: list):
        self.page.comboBox_search.addItems(fields)

    def _set_filter_orders(self, orders: List[Order]):
        self.filter_orders = orders

    def _set_filter_fields(self):
        self.th_search = QThread()
        self.worker = WorkerSearch()
        # config worker
        self.worker.orders = self.orders
        self.worker.moveToThread(self.th_search)
        self.worker.setProgessBar.connect(self._set_value_progressBar)
        self.worker.setComboBox.connect(self._set_value_comboBox)
        self.worker.finish.connect(self.th_search.quit)
        self.worker.finish.connect(self.worker.deleteLater)
        self.worker.finish.connect(self._set_filter)
        # config thread
        self.th_search.started.connect(self.worker.run)
        self.th_search.finished.connect(self.th_search.deleteLater)
        self.th_search.start()


    def _search_orders(self):
        field = self.page.comboBox_search.currentText()
        search = self.page.lineEdit_search.text()
        if not field or not search:
            return

        self.th_filter = QThread()
        self.worker = WorkerFilter()
        # config worker
        self.worker.field = field
        self.worker.search = search
        self.worker.orders = self.orders
        self.worker.moveToThread(self.th_filter)
        self.worker.setProgessBar.connect(self._set_value_progressBar)
        self.worker.setFilter.connect(self._set_filter_orders)
        self.worker.finish.connect(self.th_filter.quit)
        self.worker.finish.connect(self.worker.deleteLater)
        self.worker.finish.connect(self._set_orders)
        self.worker.finish.connect(lambda: self.page.btn_s_h_o.setEnabled(True))
        # config thread
        self.th_filter.started.connect(self.worker.run)
        self.th_filter.finished.connect(self.th_filter.deleteLater)
        self.th_filter.start()
        self.page.btn_s_h_o.setEnabled(False)
        

    def _set_filter(self, search=None):
        self.page.radio_all.setCheckable(True)
        self.page.radio_open.setCheckable(True)
        self.page.radio_close.setCheckable(True)
        options = {1: True, 2: False}
        orders = []
        for order in self.orders:
            if search is not None:
                if order.status == options[search]:
                    orders.append(order)
            else:
                orders.append(order)
        self.filter_orders = orders
        self._set_orders()

    def _set_orders(self):
        self.page.table_history_order.setRowCount(0)
        for i, order in enumerate(self.filter_orders):
            items = []
            _json = order.data_json.replace("'", '"')
            data_json = json.loads(_json)
            name_cliente = data_json['Dados do Cliente']['Nome Completo']
            items.append(str(order.id))
            items.append(name_cliente)
            if order.status:
                items.append('Aberta')
            else:
                items.append('Finalizado')
            items.append(order.date)
            self.page.table_history_order.insertRow(self.page.table_history_order.rowCount())
            for y in range(self.page.table_history_order.columnCount()):
                item = QTableWidgetItem(items[y])
                self.page.table_history_order.setItem(i, y, item)
                self.page.table_history_order.item(i, y).setData(Qt.UserRole, Qt.PointingHandCursor)
                self.page.table_history_order.item(i,y).setToolTip('Clique duas vezes para abrir a ordem!')
             
    def _item_clicked(self, item: QTableWidgetItem):
        order = self.filter_orders[item.row()]
        pdf_view = PDFPage(order)
        pdf_view.update_status = self._set_filter
        pdf_view.remove_order = self._remove_order_list
        pdf_view.show()
        pdf_view.hide(self.page)

    def _change_cursor(self, item):
        cursor = item.data(Qt.UserRole)
        if cursor:
            self.page.table_history_order.viewport().setCursor(cursor)
        else:
            self.page.table_history_order.viewport().unsetCursor()
            
    def _remove_orders(self):
        self.page.table_history_order.setRowCount(0)

    def _remove_filter(self):
        self.page.radio_all.setCheckable(False)
        self.page.radio_open.setCheckable(False)
        self.page.radio_close.setCheckable(False)


class WorkerSearch(QObject):
    finish = Signal()
    setProgessBar = Signal(int)
    setComboBox = Signal(list)
    orders: List[Order] = None

    def run(self):
        self.setProgessBar.emit(0)
        total = len(self.orders)
        fields = {}
        for i, order in enumerate(self.orders):
            _json = order.data_json.replace("'", '"')
            data_json = json.loads(_json)
            for key in data_json:
                for subkey in data_json[key]:
                    if not subkey in fields:
                        fields[subkey] = True
            value = int(((i+1)/total)*100)
            self.setProgessBar.emit(value)

        self.setComboBox.emit([k for k in fields])
        self.finish.emit()


class WorkerFilter(QObject):
    field = str
    search = str
    orders: List[Order] = None
    finish = Signal()
    setProgessBar = Signal(int)
    setFilter = Signal(list)

    def run(self):
        print('run')
        self.setProgessBar.emit(0)
        total = len(self.orders)
        results = []
        for i, order in enumerate(self.orders):
            _json = order.data_json.replace("'", '"')
            data_json = json.loads(_json)
            for key in data_json:
                if self.field in data_json[key]:
                    f_lower = str(data_json[key][self.field]).lower()
                    if self.search.lower() in f_lower:
                        results.append(order)
                value = int(((i+1)/total)*100)
                self.setProgessBar.emit(value)
            
        self.setFilter.emit(results)
        self.finish.emit()

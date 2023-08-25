import json
from typing import List
from src.application.infra.pyside.ui.core import QTableWidgetItem, Qt, QToolTip, QFont
from src.application.infra.pyside.page.main_window import Ui_MainWindow
from src.application.infra.sqlite.crud_order import get_orders
from src.application.infra.pyside.page.pdf_page import PDFPage
from src.domain.entity.order import Order


class HistoryPage:

    def __init__(self, main_page: Ui_MainWindow) -> None:
        self.page = main_page
        self.orders: List[Order] = None
        self.filter_orders: List[Order] = None

    def assemble(self, search=None):
        self.page.stackedWidget.setCurrentIndex(3)
        self.page.radio_all.clicked.connect(lambda: self._set_filter(None))
        self.page.radio_open.clicked.connect(lambda: self._set_filter(1))
        self.page.radio_close.clicked.connect(lambda: self._set_filter(2))
        self.page.table_history_order.itemEntered.connect(self._change_cursor)
        self.page.table_history_order.itemDoubleClicked.connect(self._item_clicked)
        self.page.lineEdit_search.textChanged.connect(self._search_line)
        self._get_orders()
        self._set_filter(search)   
        
    def disassemble(self):
        self.orders = None
        self.filter_orders = None
        self.page.table_history_order.itemEntered.disconnect(self._change_cursor)
        self.page.table_history_order.itemDoubleClicked.disconnect(self._item_clicked)
        self._remove_orders()
        self._remove_filter()

    def _remove_order_list(self, order: Order):
        self.orders.remove(order)
        self.filter_orders.remove(order)

    def _get_orders(self):
        self.orders = get_orders()

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

    def _search_line(self, text: str):
        aux = self.filter_orders
        search = []
        for order in self.filter_orders:
            _json = order.data_json.replace("'", '"')
            data_json = json.loads(_json)
            name_cliente: str = data_json['Dados do Cliente']['Nome Completo']
            if text.lower() in name_cliente.lower() or text.lower() in order.date.lower():
                search.append(order)
            try:
                if int(text) == order.id and not order in search:
                    search.append(order)
            except:
                pass

        self.filter_orders = search
        self._set_orders()
        self.filter_orders = aux


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

        
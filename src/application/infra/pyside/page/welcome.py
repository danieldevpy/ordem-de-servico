from src.application.infra.pyside.page.main_window import Ui_MainWindow
from src.application.infra.sqlite.crud_order import get_info_orders
from src.application.infra.pyside.controller.routes import Routes

class WelcomePage:

    def __init__(self, main_page: Ui_MainWindow) -> None:
        self.page = main_page
        self.route = Routes()

    def assemble(self):
        self._set_informations()
        self.page.stackedWidget.setCurrentIndex(0)
        self.page.actionVoltar_para_tela_inicial.setVisible(False)
        self.page.info_orders.clicked.connect(lambda: self.route.navigate('history'))
        self.page.info_orders_open.clicked.connect(lambda: self.route.navigate('history', 1))
        self.page.info_orders_close.clicked.connect(lambda: self.route.navigate('history', 2))

    def disassemble(self):
        self.page.info_orders.setText('0')
        self.page.info_orders_open.setText('0')
        self.page.info_orders_close.setText('0')
        self.page.actionVoltar_para_tela_inicial.setVisible(True)
        self.page.info_orders.clicked.disconnect()
        self.page.info_orders_open.clicked.disconnect()
        self.page.info_orders_close.clicked.disconnect()

    def _set_informations(self):
        infos = get_info_orders()
        self.page.info_orders.setText(str(infos['all']))
        self.page.info_orders_open.setText(str(infos['open']))
        self.page.info_orders_close.setText(str(infos['close']))
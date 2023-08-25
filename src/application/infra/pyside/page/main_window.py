from sqlmodel import Session, select, delete
from src.application.infra.pyside.ui.core import QMainWindow, Qt, QAbstractItemView
from src.application.infra.pyside.ui.mainwindow import Ui_MainWindow
from src.application.infra.pyside.page.welcome import WelcomePage
from src.application.infra.pyside.page.layout_order import LayoutOrderPage
from src.application.infra.pyside.page.register_order import RegisterOrderPage
from src.application.infra.pyside.page.history_order import HistoryPage
from src.application.infra.pyside.controller.routes import Routes


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema Ordem de Serviço')
        self._welcome = WelcomePage(main_page=self)
        self.route = Routes()
        self.__configs()
        self.__register()

    def __configs(self):
        self.actionVisualizar_Layout.setVisible(False)
        self.table_categoria.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_categoria.setSelectionBehavior(QAbstractItemView.SelectRows)

    def __register(self):
        self.route.config_welcome(self._welcome)
        self.route.register_page(name_route=self.btn_r_o.objectName(), page=RegisterOrderPage(main_page=self))
        self.route.register_page(name_route='layout_order', page=LayoutOrderPage(main_page=self))
        self.route.register_page(name_route='history', page=HistoryPage(main_page=self))
        self.btn_r_o.clicked.connect(lambda: self.route.navigate(self.btn_r_o.objectName()))
        self.btn_h_o.clicked.connect(lambda: self.route.navigate('history', None))
        self.btn_e_o.clicked.connect(lambda: self.route.navigate('layout_order'))
        self.actionVoltar_para_tela_inicial.triggered.connect(lambda: self.route.navigate('welcome'))
        self.actionLayout_Ordens.triggered.connect(lambda: self.route.navigate('layout_order'))
        self.actionVisualizar_Layout.triggered.connect(lambda: self.route.navigate(self.btn_r_o.objectName()))

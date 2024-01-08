from src.application.infra.pyside.ui.core import *
from src.application.infra.pyside.page.main_window import Ui_MainWindow
import time

class EditOrderPage(QMainWindow):

    def __init__(self, back_page: QMainWindow):
        self.page = back_page
        super(EditOrderPage, self).__init__()
        self.setWindowTitle("Visualizar Ordem")
        self.setGeometry(0, 28, 1000, 750)
        self.resize(1061, 614)
        time.sleep(5)
        back_page.show()
        back_page.descobrindo()
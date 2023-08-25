from abc import ABC, abstractmethod
from src.application.infra.pyside.ui.mainwindow import Ui_MainWindow


class PageRepository(ABC):

    def __init__(self, page:Ui_MainWindow) -> None:
        self.page = page

    @abstractmethod
    def assemble(self):
        pass

    @abstractmethod
    def disassemble(self):
        pass

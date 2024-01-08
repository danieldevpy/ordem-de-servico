from src.application.infra.pyside.ui.core import QApplication
from src.application.infra.pyside.page.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showNormal()
    sys.exit(app.exec())
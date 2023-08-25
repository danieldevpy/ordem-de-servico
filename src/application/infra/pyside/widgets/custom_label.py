from src.application.infra.pyside.ui.core import QLabel


class CustomLabel(QLabel):
    def __init__(self, parent=None, name: str = None, title=False):
        super(CustomLabel, self).__init__(parent)
        self.setObjectName(u"label_"+name)
        self.setText(name.upper())
        if title:
            self.setStyleSheet("color: rgb(61, 56, 70);;;font-size: 20px;")
        else:
            self.setStyleSheet("color: rgb(36, 31, 49);font-size: 16px;")
            
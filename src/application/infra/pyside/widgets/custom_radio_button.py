from src.application.infra.pyside.ui.core import QRadioButton


class CustomRadioButtom(QRadioButton):
    def __init__(self, parent=None, name: str = None):
        super(CustomRadioButtom, self).__init__(parent)
        print(name)
        self.setObjectName(u"radio_"+name)
        self.setText(name)
        self.setStyleSheet("color: black;")

    def clear_object(self):
        return
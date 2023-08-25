from src.application.infra.pyside.ui.core import QLineEdit


class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None, name: str = None):
        super(CustomLineEdit, self).__init__(parent)
        self.setObjectName(u"line_"+name)

    def get_text_object(self):
        return self.text()
    
    def clear_object(self):
        self.clear()
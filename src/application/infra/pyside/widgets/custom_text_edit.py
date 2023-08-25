from src.application.infra.pyside.ui.core import QPlainTextEdit


class CustomPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None, name: str = None):
        super(CustomPlainTextEdit, self).__init__(parent)
        self.setObjectName(u"plain_"+name)
        
    def get_text_object(self):
        return self.toPlainText()
    
    def clear_object(self):
        self.clear()
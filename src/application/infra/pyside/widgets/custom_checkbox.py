from src.application.infra.pyside.ui.core import QCheckBox


class CustomCheckBox(QCheckBox):
    def __init__(self, parent=None, name: str = None):
        super(CustomCheckBox, self).__init__(parent)
        self.setObjectName(u"check_"+name)
        self.setStyleSheet("color: black;")
        self.setText(name)

    def clear_object(self):
        return
    
    def get_text_object(self):
        if self.isChecked():
            return "✓"
        else:
            return "✗"
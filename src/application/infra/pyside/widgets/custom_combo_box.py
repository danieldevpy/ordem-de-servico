

from typing import List
from src.application.infra.pyside.ui.core import QComboBox


class CustomComboBox(QComboBox):
    def __init__(self, parent=None, name: str = None):
        super(CustomComboBox, self).__init__(parent)
        self.setObjectName(u"combo_"+name)


    def get_text_object(self):
        return self.currentText()
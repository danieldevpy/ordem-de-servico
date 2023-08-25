from src.application.infra.pyside.ui.core import QWidget


class CustomWidget(QWidget):
     def __init__(self, parent=None, name: str = None):
        super(CustomWidget, self).__init__(parent)
        self.setObjectName(u"widget_"+name)
        # Seu código personalizado para o QWidget
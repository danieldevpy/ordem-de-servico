from src.application.infra.pyside.ui.core import QFrame


class CustomFrame(QFrame):
    def __init__(self, parent=None, name: str = None):
        super(CustomFrame, self).__init__(parent)
        self.setObjectName(u"frame_"+name)
        # Seu código personalizado para o QFrame
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        #self.setStyleSheet("QFrame{border:none;}")

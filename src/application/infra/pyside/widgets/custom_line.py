from src.application.infra.pyside.ui.core import QWidget, QFrame, QVBoxLayout


class CustomLine(QWidget):
    def __init__(self, parent=None, name: str = None):
        super(CustomLine, self).__init__(parent)

        # Criar um objeto QFrame e definir o tipo de frame como um separador horizontal
        horizontal_line = QFrame()
        horizontal_line.setFrameShape(QFrame.Shape.HLine)
        horizontal_line.setFrameShadow(QFrame.Shadow.Sunken)

        # Layout vertical para o widget
        layout = QVBoxLayout()
        layout.addWidget(horizontal_line)
        self.setLayout(layout)

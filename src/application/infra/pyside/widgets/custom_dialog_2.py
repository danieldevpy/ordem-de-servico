from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton
from src.application.infra.pyside.widgets.register_widgets import RegisterWidgets
from src.application.infra.pyside.widgets.custom_combo_box import CustomComboBox


class CustomDialog2(QDialog):
    def __init__(self, text: str, name_field: str, event_function: list, extra = None, text2 = None, name_field2 = None):
        super().__init__()
        self.text = text
        self.name_field = name_field
        self.event_function = event_function
        self.extra = extra
        self.text2 = text2
        self.name_field2 = name_field2
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Adiciona QLabel para orientar o usuário
        label1 = QLabel(self.text)
        self.text_input1 = QLineEdit()
        self.text_input1.setText(self.name_field)
        layout.addWidget(label1)
        layout.addWidget(self.text_input1)

        if self.extra:
            label2 = QLabel(self.text2)
            self.combo_box = CustomComboBox(parent=None, name="field")
            self.combo_box.addItems(RegisterWidgets.get_keys())
            self.combo_box.setCurrentText(self.name_field2)
            layout.addWidget(label2)
            layout.addWidget(self.combo_box)


        # Adiciona os botões de opção
        button1 = QPushButton("APLICAR ALTERAÇÕES")
        button2 = QPushButton("DELETAR")
        button3 = QPushButton("CANCELAR")

        button1.clicked.connect(lambda: self.onButtonClicked(0))
        button2.clicked.connect(lambda: self.onButtonClicked(1))
        button3.clicked.connect(lambda: self.onButtonClicked(1, cancel=True))

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setLayout(layout)

    def onButtonClicked(self, option, cancel = False):
        if cancel:
            self.accept()
            return

        if not self.extra:
            name = self.text_input1.text()
            self.event_function[option](name)
            self.accept()
            return
        else:
            name1 = self.text_input1.text()
            name2 = self.combo_box.currentText()
            self.event_function[option](name1, name2)
            self.accept()
            return
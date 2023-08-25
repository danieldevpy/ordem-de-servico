from src.application.infra.pyside.ui.core import *
from src.application.infra.pyside.widgets.custom_messages import show_message, show_message_with_confirmation
from PySide6.QtWebEngineWidgets import QWebEngineView
from src.domain.entity.order import Order
from src.application.infra.pdf.generate_pdf import GeneratePdfHTML
from src.application.infra.sqlite.crud_order import update_order, delete_order

class PDFPage(QMainWindow):
    
    def __init__(self, order: Order):
        super(PDFPage, self).__init__()
        self.setWindowTitle("Visualizar Ordem")
        self.setGeometry(0, 28, 1000, 750)
        self.resize(1061, 614)
        self.update_status = None
        self.remove_order = None
        self.order = order
        self.pdf_html, self.buffer = GeneratePdfHTML.generate(order)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.webView = QWebEngineView()
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy1)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.layout.addWidget(self.webView)

        self.label = QLabel("Status da Ordem")
        self.r1 = QRadioButton()
        self.r2 = QRadioButton()

        self.r1.setText("Em Aberto")
        self.r2.setText("Finalizada")

        self.r1.clicked.connect(self._radio_set_true)
        self.r2.clicked.connect(self._radio_set_false)

        self.button = QPushButton("Salvar Arquivo PDF")
        self.button.clicked.connect(self._save_pdf)

        self.delet = QPushButton("Deletar Ordem de Serviço")
        self.delet.clicked.connect(self._delete_order)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.r1)
        self.layout.addWidget(self.r2)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.delet)

        self.webView.setHtml(self.pdf_html)

        self._check_radio()

    def _check_radio(self):
        if self.order.status:
            self.r1.setChecked(True)
        else:
            self.r2.setChecked(True)

    def _radio_set_true(self):
        self.order.status = True
        update_order(self.order)
        self._update()

    def _radio_set_false(self):
        self.order.status = False
        update_order(self.order)
        self._update()

    def _update(self):
        if self.update_status:
            self.update_status()

    def _delete_order(self):
        reponse = show_message_with_confirmation("information", "Deletar Ordem", "Você realmente deseja deletar essa ordem?")
        if not reponse:
            return
        delete_order(self.order)
        if self.remove_order:
            self.remove_order(self.order)
        self._update()
        self.close()


    def _save_pdf(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly  # Somente exibir diretórios

        folder = QFileDialog.getExistingDirectory(
            self, "Escolha uma pasta para salvar", options=options)

        if folder:
            with open(folder+f"/order-{self.order.id}.pdf", "wb") as pdf_file:
                pdf_file.write(self.buffer)
            show_message("sucess", "Arquivo Salvo", "O pdf foi salvo com sucesso na pasta: "+ folder)
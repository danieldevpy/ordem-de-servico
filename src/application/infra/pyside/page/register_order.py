from src.application.infra.pyside.ui.core import QSpacerItem, QSizePolicy
from src.application.infra.pyside.page.main_window import Ui_MainWindow
from src.application.infra.pyside.controller.create_fields import CreateFields
from src.application.infra.sqlite import crud_categorys, crud_clientes, crud_order
from src.application.infra.pyside.widgets.custom_messages import show_message
from datetime import datetime


class RegisterOrderPage:

    def __init__(self, main_page: Ui_MainWindow) -> None:
        self.page = main_page
        self.clientes = {'selected': None, 'list': None}
        self.memory = {'entity': None, 'widget': None}
        self._objs = []
        self.fields = None
        self.widgets = None

    def assemble(self):
        self.page.stackedWidget.setCurrentIndex(1)
        self.page.frame_make.setVisible(False)
        #functions
        self._config_widgets() # essa função configura a conexão dos widgets com as funções
        self._set_date() # função para setar data na interface
        self._set_clientes() # função para setar os clientes no combobox e estruturas de dados (self.clientes)
        self._create_fields() # função para criar os campos (widgets da interface)

    def disassemble(self):
        self.page.frame_make.setVisible(True)
        #functions
        self._clear_texts()
        self._remove_clientes()
        self._remove_fields()
        self._desconfig_widgets()

    def _set_date(self):
        self.page.label_data.setText(datetime.now().strftime("Data: %d/%m/%Y"))

    def _create_fields(self):
        categorys = crud_categorys.get_categorys()
        
        self.fields = {}
        self.fields["Dados do Cliente"] = {
            "Nome Completo": self.page.line_nome_completo,
            "Celular": self.page.line_celular_cliente
            }
        fields, self.widgets = CreateFields.create(categorys=categorys, layout=self.page.verticalLayout_16)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self._objs.append(spacer)
        self.page.verticalLayout_16.addItem(spacer)
        self.fields.update(fields)

    def _remove_fields(self):
        if self.widgets:
            for widget in self.widgets:
                [children.deleteLater() for children in widget.children()]
                self.page.verticalLayout_16.removeWidget(widget)
            [self.page.verticalLayout_16.removeItem(obj) for obj in self._objs]
            self.widgets = None

    def _set_clientes(self):
        self.clientes['list'] = crud_clientes.get_clientes()
        self.page.comboBox_cliente.addItem("Cliente Novo")
        self.page.comboBox_cliente.addItems([cliente.name for cliente in self.clientes['list']])
    
    def _remove_clientes(self):
        self.clientes = {'selected': None, 'list': None}
        self.memory = {'entity': None, 'widget': None}
        self.page.comboBox_cliente.clear()

    def _config_widgets(self):
        self.page.btn_gravar.clicked.connect(self._create_order)
        self.page.comboBox_cliente.currentIndexChanged.connect(self._combobox_changed)
        self.page.btn_save_cliente.clicked.connect(self._save_cliente)
        self.page.btn_del_cliente.clicked.connect(self._del_cliente_)


    def _desconfig_widgets(self):
        self.page.btn_gravar.clicked.disconnect(self._create_order)
        self.page.comboBox_cliente.currentIndexChanged.disconnect(self._combobox_changed)
        self.page.btn_save_cliente.clicked.disconnect(self._save_cliente)
        self.page.btn_del_cliente.clicked.disconnect(self._del_cliente_)

    def _clear_texts(self):
        if self.fields:
            for category in self.fields:
                for field in self.fields[category]:
                    widget = self.fields[category][field]
                    try:
                        widget.clear()
                    except:
                        widget.clear_object()
                        
        self.page.comboBox_cliente.setCurrentIndex(0)

    
    def _combobox_changed(self):
        if self.page.comboBox_cliente.count() == 0:
            return
        index = self.page.comboBox_cliente.currentIndex()
        
        if index > 0:
            cliente = self.clientes['list'][index-1]
            self.clientes['selected'] = cliente
            self.memory['widget'] = index
            self.page.line_nome_completo.setText(cliente.name)
            self.page.line_celular_cliente.setText(cliente.cel)
            self.page.btn_save_cliente.setText("ATUALIZAR DADOS DO CLIENTE")
            self.page.btn_del_cliente.setVisible(True)
        else:
            self.clientes['selected'] = None
            self.page.line_nome_completo.setText("")
            self.page.line_celular_cliente.setText("")
            self.page.btn_save_cliente.setText("SALVAR NOVO CLIENTE")
            self.page.btn_del_cliente.setVisible(False)


    def _save_cliente(self):
        cliente = self.clientes['selected']
        if cliente:
            cliente.name = self.page.line_nome_completo.text()
            cliente.cel = self.page.line_celular_cliente.text()
            crud_clientes.update_cliente(cliente)
            self.page.comboBox_cliente.setItemText(self.memory['widget'], cliente.name)
            show_message("sucess", "Atualizar Cliente", f"O cliente {cliente.name} foi atualizado!")
        else:
            name = self.page.line_nome_completo.text()
            cel = self.page.line_celular_cliente.text()
            if name:
                c = crud_clientes.add_cliente_fields(name=name, cel=cel)
                self.clientes['list'].append(c)
                self.page.comboBox_cliente.addItem(c.name)
                self.page.comboBox_cliente.setCurrentIndex(self.page.comboBox_cliente.count()-1)
                show_message("sucess", "Registrar Cliente", f"O cliente {name} foi registrado!")

    def _del_cliente_(self):
        cliente = self.clientes['selected']
        if not cliente:
            return
        response = crud_clientes.del_cliente(cliente)
        if not response:
            print("error")
        self.page.comboBox_cliente.removeItem(self.page.comboBox_cliente.currentIndex())
        self.page.comboBox_cliente.setCurrentIndex(0)
       

    def _create_order(self):
        order = {}
        if self.fields:
            for category in self.fields:
               
                for field in self.fields[category]:
                    text = None
                    widget = self.fields[category][field]
                    try:
                        text = widget.get_text_object()
                    except:
                        text = widget.text()
                    if text:
                        if not category in order:
                            order[category] = {}
                        order[category][field] = text
 
        id_ordem, err = crud_order.create_order(str(order))
        if id_ordem:
            show_message('sucess', 'Sucesso', f'Ordem registrada com sucesso! ID: {id_ordem}')
            self._clear_texts()
        else:
            show_message('error', 'Erro', f'Não foi possivel registrar essa ordem, error: {err}')
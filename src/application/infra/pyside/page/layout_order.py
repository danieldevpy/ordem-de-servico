from typing import List
from src.application.infra.sqlite import crud_categorys, crud_fields
from src.application.infra.pyside.ui.core import QListWidgetItem, QTableWidgetItem, QMenu, Qt, QAbstractItemView, QInputDialog
from src.application.infra.pyside.page.main_window import Ui_MainWindow
from src.application.infra.pyside.widgets.custom_dialog import CustomDialog
from src.application.infra.pyside.widgets.custom_dialog_2 import CustomDialog2
from src.application.repository.pageRepository import PageRepository
from src.application.infra.pyside.widgets.custom_messages import show_message, show_message_with_confirmation, get_text
from src.domain.entity.fields import Fields

class LayoutOrderPage(PageRepository):

    def __init__(self, main_page: Ui_MainWindow) -> None:
        super().__init__(main_page)
        self.categorys = {'selected': None, 'list': {}}
        self.memory = {'category': {'entity': None, 'widget': None, 'indexs': None}}

    def assemble(self):
        self.page.stackedWidget.setCurrentIndex(2)
        self.page.actionLayout_Ordens.setVisible(False)
        self.page.actionVisualizar_Layout.setVisible(True)
        self.page.table_categoria.setVisible(False)
        self.page.list_categoria.itemDoubleClicked.connect(self._selected_category)
        self.page.table_categoria.customContextMenuRequested.connect(self._table_event)
        self.page.btn_create_categoria.clicked.connect(self._create_category)
        self.page.btn_edit_categoria.clicked.connect(self._edit_category)
        self.page.btn_pos_categoria.clicked.connect(self._invert_position)
        # # functions
        self._set_categorys()


    def disassemble(self):
        self.page.actionLayout_Ordens.setVisible(True)
        self.page.actionVisualizar_Layout.setVisible(False)
        self.page.list_categoria.itemDoubleClicked.disconnect(self._selected_category)
        self.page.table_categoria.customContextMenuRequested.disconnect(self._table_event)
        self.page.btn_create_categoria.clicked.disconnect(self._create_category)
        self.page.btn_edit_categoria.clicked.disconnect(self._edit_category)
        self.page.btn_pos_categoria.clicked.disconnect(self._invert_position)
        self._remove_states()

        # # functions
    def _remove_states(self):
        self.categorys = {'selected': None, 'list': {}}
        self.memory = {'category': {'entity': None, 'widget': None, 'indexs': None}}
        self.page.label_category_layout.setText("")
        self.page.table_categoria.setRowCount(0)

    def _set_categorys(self):
        self.page.list_categoria.clear()
        categorys = crud_categorys.get_categorys()
        for category in categorys:
            self.categorys['list'][category.name] = category
        self.page.list_categoria.addItems([category.name for category in categorys])

    def _selected_category(self, item: QListWidgetItem):
        self.memory = {'category': {'entity': None, 'widget': None, 'indexs': None}}
        category = self.categorys['list'][item.text()]
        self.categorys['selected'] = category
        self.memory['category']['widget'] = item
        self.page.label_category_layout.setText(category.name)
        self.page.table_categoria.setVisible(True)
        self._set_table(category.fields)


    def _set_table(self, fields: List[Fields]):
        self.page.table_categoria.setRowCount(0)
        if fields:
            for i, field in enumerate(fields):
                self.page.table_categoria.insertRow(self.page.table_categoria.rowCount())
                name = QTableWidgetItem(field.name)
                type_field = QTableWidgetItem(field.type_field)
                self.page.table_categoria.setItem(i, 0, name)
                self.page.table_categoria.setItem(i, 1, type_field)

    def _table_event(self, pos):
        context_menu = QMenu(self.page)
        action_create_field = None
        action_edit_field = None
        action_desselect_field = None
        index_selected = self.page.table_categoria.selectedIndexes()
        items_selected = self.page.table_categoria.selectedItems()

        if self.categorys['selected'] is not None and len(index_selected) == 0:
            action_create_field = context_menu.addAction("Adicionar Campo")
        elif len(items_selected) > 0:
            action_edit_field = context_menu.addAction(f"Editar campo: {items_selected[0].text()}")
            action_desselect_field = context_menu.addAction(f"Desselecionar campo")

        global_pos = self.page.table_categoria.mapToGlobal(pos)
        selected_action = context_menu.exec(global_pos)

        if selected_action is not None:
            if selected_action == action_create_field:
                self._create_field()
            elif selected_action == action_edit_field:
                self._edit_field(items_selected)
            elif selected_action == action_desselect_field:
                self.page.table_categoria.clearSelection()

    def _create_category(self):
        name, ok = get_text("Criar Categoria", "Digite o nome da categoria:")
        if ok:
            category, err = crud_categorys.create_category(name=name)
            if err:
                print('error')
            else:
                category.fields = []
                self.categorys['list'][category.name] = category
                self.page.list_categoria.addItem(category.name)

    def _edit_category(self):
        index = self.page.list_categoria.selectedItems()
        if len(index) > 1 or not index:
            show_message('error', 'Erro na operação', 'Selecione uma categoria, para realizar a edição')
            return
        self.memory['category']['entity'] = self.categorys['list'][index[0].text()]
        self.memory['category']['widget'] = index[0]
        dialog = CustomDialog("Nome da Categoria", index[0].text(), [self._rename_category, self._delete_category])
        dialog.exec_()

    def _rename_category(self, name:str):
        category = self.memory['category']['entity']
        category.name = name
        crud_categorys.update_category(category, category.id)
        self.categorys['list'][category.name] = category
        widget = self.memory['category']['widget']
        widget.setText(name)
        self.page.label_category_layout.setText(category.name)
        show_message('sucess', 'Renoemar Categoria', 'A categoria foi renomeada com sucesso!')

    def _delete_category(self, name=None):
        response = show_message_with_confirmation('information', 'Remover Categoria', 'Deseja realmente excluir essa categoria?')
        if not response:
            return
        try:
            category = self.memory['category']['entity']
            if category.fields:
                for field in category.fields:
                    crud_fields.delete_field(field)
            crud_categorys.delete_category(category)
            self.page.table_categoria.setRowCount(0)
            if category.name == self.page.label_category_layout.text():
                self.page.table_categoria.setVisible(False)
            self.categorys['selected'] = None
            self.page.label_category_layout.setText("")
            self.page.list_categoria.takeItem(self.page.list_categoria.row(self.memory['category']['widget']))
            show_message("sucess", "Remover Categoria", "A categoria foi removida com sucesso!")
        except:
            show_message("error", "Remover Categoria", "Não foi possivel remover a categoria")



    def _invert_position(self):
        index = self.page.list_categoria.selectedItems()
        if len(index) != 2:
            show_message('error', 'Erro na operação', 'Selecione duas categorias, para inverter a ordem')
            return
        
        c1 = self.categorys['list'][index[0].text()]
        c2 = self.categorys['list'][index[1].text()]

        response = show_message_with_confirmation('information', 'Trocar ordem', f'Trocar ordem de \n{c1.name} * \npor \n{c2.name} *')
        if not response:
            return
        
        aux1 = c1.id
        aux2 = c2.id
        aux3 = 9999

        c2.id = aux3
        c1.id = aux2

        crud_categorys.update_category(c2, aux2)
        crud_categorys.update_category(c1, aux1)
        c2.id = aux1
        crud_categorys.update_category(c2, aux3)

        if c1.fields:
            for field in c1.fields:
                field.category_id = c1.id
                crud_fields.update_fields(field, field.id)
                
        if c2.fields:
            for field in c2.fields:
                field.category_id = c2.id
                crud_fields.update_fields(field, field.id)

        index[0].setText(c2.name)
        index[1].setText(c1.name)

        show_message('sucess', 'Trocar ordem', 'A troca foi realizada com sucesso!')
        

    def _create_field(self):
        category = self.categorys['selected']
        name, ok = get_text("Criar campo de texto", "Digite o nome do campo")
        if not ok or len(name) < 1:
            return
        field = Fields(id=0, name=name, type_field='texto curto', category_id=category.id)
        field = crud_fields.create_field(field)
        if not field:
            return
        category.fields.append(field)
        widget_category = self.memory['category']['widget'] 
        self._selected_category(widget_category)
        
    def _edit_field(self, items_selected):
        
        names = [item.text() for item in items_selected]
        self.memory['category']['indexs'] = [item.row() for item in items_selected]
        dialog = CustomDialog2("Nome da Categoria", names[0], [self._rename_field, self._delete_field], True, "Tipo de dado", names[1])
        dialog.exec_()


    def _rename_field(self, name, type_field):
        category = self.categorys['selected']
        index = self.memory['category']['indexs'][0]

        if not category.fields:
            return
        
        field = category.fields[index]
        field.name = name
        field.type_field = type_field
        crud_fields.update_fields(field, field.id)
        self.page.table_categoria.item(index, 0).setText(name)
        self.page.table_categoria.item(index, 1).setText(type_field)
        
    def _delete_field(self, name=None, type_field = None):
        try:
            category = self.categorys['selected']
            index = self.memory['category']['indexs'][0]
            if not category.fields:
                return
            field = category.fields[index]
            crud_fields.delete_field(field)
            self.page.table_categoria.removeRow(index)
            show_message("sucess", "Remover Campo", "o campo foi removido com sucesso!")
        except:
            show_message("error", "Erro ao remover", "erro ao remover o campo")

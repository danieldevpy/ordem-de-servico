from src.application.infra.pyside.ui.core import QListWidget, QInputDialog, Qt, QListWidgetItem, QAbstractItemView
from src.application.infra.pyside.widgets.custom_messages import get_text
from src.application.infra.pyside.widgets.custom_dialog import CustomDialog

class CustomListWidget(QListWidget):
    def __init__(self, parent=None, name: str = None):
        super(CustomListWidget, self).__init__(parent)
        self.setObjectName(u"list_"+name)
        self.setCursor(Qt.PointingHandCursor)
        self.memory = None
        # Conecte o sinal itemDoubleClicked ao slot addItemOnDoubleClick
        #self.itemDoubleClicked.connect(self.edit_item)

    def mouseDoubleClickEvent(self, event):
        item = self.itemAt(event.pos())
        if item is None:
            new_item_text, ok = get_text("Adicionar Item", "Digite o novo item:")
            if ok and new_item_text:
                new_item = QListWidgetItem(f'({self.count()+1}) {new_item_text}')
                self.addItem(new_item)
                self.scrollToItem(new_item, QAbstractItemView.ScrollHint.EnsureVisible)

        else:
            self.memory = item
            dialog = CustomDialog(f"Alterar item: {item.text()}", item.text(), [self.edit_item, self.remove_item])
            dialog.exec_()
            super().mouseDoubleClickEvent(event)
    
    def reorder(self):
        pass

    def edit_item(self, item_name):
        self.memory.setText(item_name)

    def remove_item(self, name=None):
        index = self.row(self.memory)
        self.takeItem(index)
        self.memory = None
    
    def get_text_object(self):
        texts = []
        for index in range(self.count()):
            item = self.item(index)
            text = item.text()
            for i in range(len(text)):
                if text[i] == ")":
                    texts.append(text[i+2:])
        return texts
    
    def clear_object(self):
        self.clear()
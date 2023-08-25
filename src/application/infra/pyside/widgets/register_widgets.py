from src.application.infra.pyside.ui.core import QWidget
from src.application.infra.pyside.widgets.custom_lineEdit import CustomLineEdit
from src.application.infra.pyside.widgets.custom_text_edit import CustomPlainTextEdit
from src.application.infra.pyside.widgets.custom_list_widget import CustomListWidget
from src.application.infra.pyside.widgets.custom_radio_button import CustomRadioButtom
from src.application.infra.pyside.widgets.custom_checkbox import CustomCheckBox

class RegisterWidgets:

    _widgets = {}

    @classmethod
    def register(cls, name: str, widget: QWidget):
        cls._widgets[name] = widget

    @classmethod
    def get(cls, name: str):
        if name in cls._widgets:
            return cls._widgets[name]

    @classmethod  
    def get_keys(cls):
        return [name for name in cls._widgets]
        

RegisterWidgets.register("texto curto", CustomLineEdit)
RegisterWidgets.register("texto longo", CustomPlainTextEdit)
RegisterWidgets.register("lista", CustomListWidget)
RegisterWidgets.register("marcação", CustomCheckBox)
#RegisterWidgets.register("opção", CustomRadioButtom)

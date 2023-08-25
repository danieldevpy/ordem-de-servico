from src.application.infra.pyside.ui.core import QLayout, QVBoxLayout, QHBoxLayout
from src.application.infra.pyside.widgets.custom_widget import CustomWidget
from src.application.infra.pyside.widgets.custom_label import CustomLabel
from src.application.infra.pyside.widgets.custom_line import CustomLine
from src.application.infra.pyside.widgets.custom_frame import CustomFrame
from src.application.infra.pyside.widgets.register_widgets import RegisterWidgets
from src.domain.entity.fields import Fields
from src.domain.entity.category import Category

class CategoryController:

    def __init__(self, category: Category, layout: QLayout) -> None:
        self.category = category
        # header
        self.widget = CustomWidget(name=category.name)
        self.vertical_to_widget = QVBoxLayout(self.widget)
        self.label = CustomLabel(parent=self.widget, name=category.name, title=True)
        self.line = CustomLine(parent=self.widget, name=category.name)
        self.frame = CustomFrame(parent=self.widget, name=category.name)
        self.vertical_to_widget.addWidget(self.label)
        self.vertical_to_widget.addWidget(self.line)
        self.vertical_to_widget.addWidget(self.frame)
        # bottom
        self.vertical_to_frame = QVBoxLayout(self.frame)
        #  memory
        self.inputs_field = {}
        widgets_field = []
        self._create_fields()

    def _create_fields(self):
        if not self.category.fields:
            return
        count = 0
        aux_layout = None
        aux_field = None
        for field in self.category.fields:
            count += 1
            if count == 2:
                if aux_field.type_field == field.type_field:
                    new_vertical = self.create_struct(field)
                    horizontal = QHBoxLayout(self.widget)
                    horizontal.addLayout(aux_layout)
                    horizontal.addLayout(new_vertical)
                    self.vertical_to_frame.addLayout(horizontal)
                else:
                    new_vertical = self.create_struct(field)
                    self.vertical_to_frame.addLayout(aux_layout)
                    self.vertical_to_frame.addLayout(new_vertical)
                count = 0
                aux_field = None
                aux_layout = None
            else:
                aux_layout = self.create_struct(field)
                aux_field = field
        if aux_layout is not None:
            self.vertical_to_frame.addLayout(aux_layout)
            aux_layout = None
            aux_field = None

    def create_struct(self, field: Fields):
        vertical = QVBoxLayout(self.widget)
        label = CustomLabel(name=field.name)
        custom_field = RegisterWidgets.get(field.type_field)(parent=self.widget, name=field.name)
        vertical.addWidget(label, custom_field)
        return vertical
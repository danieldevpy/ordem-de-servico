from src.application.infra.pyside.widgets.custom_widget import CustomWidget
from src.application.infra.pyside.widgets.custom_label import CustomLabel
from src.application.infra.pyside.widgets.custom_line import CustomLine
from src.application.infra.pyside.widgets.custom_frame import CustomFrame
from src.application.infra.pyside.widgets.custom_lineEdit import CustomLineEdit
from src.application.infra.pyside.ui.core import QLayout,  QHBoxLayout, QVBoxLayout
from src.application.infra.pyside.widgets.register_widgets import RegisterWidgets
from typing import List
from src.domain.entity.category import Category


class CreateFields:

    @classmethod
    def create(cls, categorys: List[Category], layout: QLayout):
  
        inputs_field = {}
        widgets_field = []
        for category in categorys:
        
            inputs_field[category.name] = {}
            widget = CustomWidget(name=category.name)

            vertical_w = QVBoxLayout(widget)
       
            label = CustomLabel(parent=widget, name=category.name, title=True)
            line = CustomLine(parent=widget,name=category.name)
            frame = CustomFrame(parent=widget,name=category.name)
        
            vertical_w.addWidget(label)
            vertical_w.addWidget(line)
            vertical_w.addWidget(frame)
            
            layout.addWidget(widget)
            widgets_field.append(widget)
        
            if category.fields:
                text_short = [True for field in category.fields if field.type_field == "texto curto"]
                if len(text_short) == 2:
                
                    vertical_duple = QHBoxLayout(frame)
                    vertical_duple.setContentsMargins(0, 0, 0, 0)
                  
                    for field in category.fields:
                        vertical_layout_create = QVBoxLayout()
                        if field.type_field == "marcação":
                            custom_field = RegisterWidgets.get(field.type_field)(parent=widget, name=field.name)
                            vertical_layout_create.addWidget(custom_field)
                            inputs_field[category.name][field.name] = custom_field
                        else:
                            f_label = CustomLabel(name=field.name)
                            custom_field = RegisterWidgets.get(field.type_field)(parent=widget, name=field.name)
                            vertical_layout_create.addWidget(f_label)
                            vertical_layout_create.addWidget(custom_field)
                            inputs_field[category.name][field.name] = custom_field


                        vertical_duple.addLayout(vertical_layout_create)
                else:
                    vertical_f = QVBoxLayout(frame)
                    vertical_f.setContentsMargins(0, 0, 0, 0)
                    for field in category.fields:
                        if field.type_field == "marcação":
                            custom_field = RegisterWidgets.get(field.type_field)(parent=widget, name=field.name)
                            vertical_f.addWidget(custom_field)
                            inputs_field[category.name][field.name] = custom_field
                        else:
                            f_label = CustomLabel(name=field.name)
                            custom_field = RegisterWidgets.get(field.type_field)(parent=widget, name=field.name)
                            vertical_f.addWidget(f_label)
                            vertical_f.addWidget(custom_field)
                            inputs_field[category.name][field.name] = custom_field

        return inputs_field, widgets_field
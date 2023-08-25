# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 623)
        MainWindow.setStyleSheet(u"")
        self.actionVoltar_para_tela_inicial = QAction(MainWindow)
        self.actionVoltar_para_tela_inicial.setObjectName(u"actionVoltar_para_tela_inicial")
        self.actionLayout_Ordens = QAction(MainWindow)
        self.actionLayout_Ordens.setObjectName(u"actionLayout_Ordens")
        self.actionVisualizar_Layout = QAction(MainWindow)
        self.actionVisualizar_Layout.setObjectName(u"actionVisualizar_Layout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout_8 = QVBoxLayout(self.main_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_3 = QWidget(self.main_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.widget_3.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 20px;\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.widget_3)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget = QWidget(self.main_page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QLabel{\n"
"	color: rgb(36, 31, 49);\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton{\n"
"	background: none;\n"
"	border:none;\n"
"	font-size: 46px;\n"
"	color: rgb(94, 92, 100);\n"
"	text-align: center;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_h_order = QFrame(self.widget)
        self.frame_h_order.setObjectName(u"frame_h_order")
        self.frame_h_order.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_h_order.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 221, 218);\n"
"	border-radius: 8px;\n"
"	padding: 10px;\n"
"	max-width: 600px;\n"
"	max-height: 200px;\n"
"}")
        self.frame_h_order.setFrameShape(QFrame.StyledPanel)
        self.frame_h_order.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_h_order)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.label_3 = QLabel(self.frame_h_order)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.line_2 = QFrame(self.frame_h_order)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"height: 1px;")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_10)

        self.info_orders = QPushButton(self.frame_h_order)
        self.info_orders.setObjectName(u"info_orders")
        self.info_orders.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.info_orders)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addWidget(self.frame_h_order)

        self.frame_h_open = QFrame(self.widget)
        self.frame_h_open.setObjectName(u"frame_h_open")
        self.frame_h_open.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_h_open.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(87, 227, 137);\n"
"	border-radius: 8px;\n"
"	padding: 10px;\n"
"	max-width: 600px;\n"
"	max-height: 200px;\n"
"}")
        self.frame_h_open.setFrameShape(QFrame.StyledPanel)
        self.frame_h_open.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_h_open)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.label_6 = QLabel(self.frame_h_open)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_11.addWidget(self.label_6)

        self.line_3 = QFrame(self.frame_h_open)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"height: 1px;")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_3)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_11)

        self.info_orders_open = QPushButton(self.frame_h_open)
        self.info_orders_open.setObjectName(u"info_orders_open")
        self.info_orders_open.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.info_orders_open)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)


        self.horizontalLayout_10.addWidget(self.frame_h_open)

        self.frame_h_end = QFrame(self.widget)
        self.frame_h_end.setObjectName(u"frame_h_end")
        self.frame_h_end.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_h_end.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(248, 228, 92);\n"
"	border-radius: 8px;\n"
"	padding: 10px;\n"
"	max-width: 600px;\n"
"	max-height: 200px;\n"
"}")
        self.frame_h_end.setFrameShape(QFrame.StyledPanel)
        self.frame_h_end.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_h_end)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.label_8 = QLabel(self.frame_h_end)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)

        self.line_4 = QFrame(self.frame_h_end)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(249, 240, 107);\n"
"height: 1px;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_4)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.info_orders_close = QPushButton(self.frame_h_end)
        self.info_orders_close.setObjectName(u"info_orders_close")
        self.info_orders_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.info_orders_close)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)


        self.horizontalLayout_10.addWidget(self.frame_h_end)


        self.verticalLayout_15.addWidget(self.widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_15)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_2 = QWidget(self.main_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton{\n"
"	min-width: 200px;\n"
"	min-height: 70px;\n"
"	background-color: rgb(222, 221, 218);\n"
"	color: black;\n"
"	font-size: 16px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_2)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 20px;")

        self.verticalLayout_13.addWidget(self.label_9)

        self.line_7 = QFrame(self.widget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_r_o = QPushButton(self.widget_2)
        self.btn_r_o.setObjectName(u"btn_r_o")

        self.horizontalLayout_6.addWidget(self.btn_r_o)

        self.btn_h_o = QPushButton(self.widget_2)
        self.btn_h_o.setObjectName(u"btn_h_o")

        self.horizontalLayout_6.addWidget(self.btn_h_o)


        self.verticalLayout_13.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_e_o = QPushButton(self.widget_2)
        self.btn_e_o.setObjectName(u"btn_e_o")

        self.horizontalLayout_11.addWidget(self.btn_e_o)

        self.btn__ = QPushButton(self.widget_2)
        self.btn__.setObjectName(u"btn__")

        self.horizontalLayout_11.addWidget(self.btn__)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.widget_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.main_page)
        self.create_order = QWidget()
        self.create_order.setObjectName(u"create_order")
        self.create_order.setStyleSheet(u"QWidget{\n"
"	background-color:#f9f9f9;\n"
"\n"
"}\n"
"QComboBox{\n"
"	color: black;\n"
"	background-color: white;\n"
"	height: 30px;\n"
"	border-radius: 6px;\n"
"	border-left: 3px solid rgb(36, 31, 49);\n"
"	border-bottom: 2px solid #e1dfdf;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"       color: black; \n"
"       background-color: white; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"       background-color: red;\n"
"}\n"
"QLineEdit{\n"
"	color: black;\n"
"	background-color: rgb(246, 245, 244);\n"
"	height: 30px;\n"
"	border-radius: 6px;\n"
"	border-left: 3px solid  rgb(36, 31, 49);\n"
"	border-bottom: 2px solid #e1dfdf;\n"
"}\n"
"QPlainTextEdit{\n"
"	color: black;\n"
"	background-color: rgb(246, 245, 244);\n"
"	height: 50px;\n"
"	border-radius: 6px;\n"
"	border-bottom: 3px solid  rgb(36, 31, 49);\n"
"	border-right: 2px solid #e1dfdf;\n"
"}\n"
"QListWidget{\n"
"	color:black;\n"
"	background-color: rgb(246, 245, 244);\n"
"	border-radius: 6px;\n"
"	border-left: 3px solid  rgb(36, 31, 49);\n"
"	bor"
                        "der-right: 3px solid  rgb(36, 31, 49);\n"
"	border-bottom: 2px solid #e1dfdf;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.create_order)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.create_order)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border:none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.layout_data = QWidget()
        self.layout_data.setObjectName(u"layout_data")
        self.layout_data.setGeometry(QRect(0, 0, 350, 249))
        self.verticalLayout_16 = QVBoxLayout(self.layout_data)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_ordem_servico = QWidget(self.layout_data)
        self.widget_ordem_servico.setObjectName(u"widget_ordem_servico")
        self.verticalLayout_3 = QVBoxLayout(self.widget_ordem_servico)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_ordem = QLabel(self.widget_ordem_servico)
        self.label_ordem.setObjectName(u"label_ordem")
        font = QFont()
        font.setBold(True)
        self.label_ordem.setFont(font)
        self.label_ordem.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 24px;")

        self.horizontalLayout_2.addWidget(self.label_ordem)

        self.label_data = QLabel(self.widget_ordem_servico)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setStyleSheet(u"color: rgb(61, 56, 70);\n"
"font-size: 16px;")

        self.horizontalLayout_2.addWidget(self.label_data, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.widget_ordem_servico)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_cliente = QLabel(self.widget_ordem_servico)
        self.label_cliente.setObjectName(u"label_cliente")
        self.label_cliente.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 16px;")

        self.verticalLayout_3.addWidget(self.label_cliente)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_cliente = QComboBox(self.widget_ordem_servico)
        self.comboBox_cliente.setObjectName(u"comboBox_cliente")
        self.comboBox_cliente.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_cliente)

        self.frame_option_combo = QFrame(self.widget_ordem_servico)
        self.frame_option_combo.setObjectName(u"frame_option_combo")
        self.frame_option_combo.setStyleSheet(u"border:none;")
        self.frame_option_combo.setFrameShape(QFrame.StyledPanel)
        self.frame_option_combo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_option_combo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.widget_dados_cliente = QWidget(self.widget_ordem_servico)
        self.widget_dados_cliente.setObjectName(u"widget_dados_cliente")
        self.verticalLayout_4 = QVBoxLayout(self.widget_dados_cliente)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_dados_cliente = QLabel(self.widget_dados_cliente)
        self.label_dados_cliente.setObjectName(u"label_dados_cliente")
        self.label_dados_cliente.setStyleSheet(u"color: rgb(61, 56, 70);\n"
"font-size: 20px;")

        self.horizontalLayout.addWidget(self.label_dados_cliente)

        self.btn_save_cliente = QPushButton(self.widget_dados_cliente)
        self.btn_save_cliente.setObjectName(u"btn_save_cliente")
        self.btn_save_cliente.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"color:black;")

        self.horizontalLayout.addWidget(self.btn_save_cliente, 0, Qt.AlignRight)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.line_dados_cliente = QFrame(self.widget_dados_cliente)
        self.line_dados_cliente.setObjectName(u"line_dados_cliente")
        self.line_dados_cliente.setFrameShape(QFrame.HLine)
        self.line_dados_cliente.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_dados_cliente)

        self.layout_organizador = QHBoxLayout()
        self.layout_organizador.setObjectName(u"layout_organizador")
        self.layout_origanizador1 = QVBoxLayout()
        self.layout_origanizador1.setObjectName(u"layout_origanizador1")
        self.label = QLabel(self.widget_dados_cliente)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 16px;")

        self.layout_origanizador1.addWidget(self.label)

        self.line_nome_completo = QLineEdit(self.widget_dados_cliente)
        self.line_nome_completo.setObjectName(u"line_nome_completo")

        self.layout_origanizador1.addWidget(self.line_nome_completo)


        self.layout_organizador.addLayout(self.layout_origanizador1)

        self.layout_origanizador2 = QVBoxLayout()
        self.layout_origanizador2.setObjectName(u"layout_origanizador2")
        self.label_2 = QLabel(self.widget_dados_cliente)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 16px;")

        self.layout_origanizador2.addWidget(self.label_2)

        self.line_celular_cliente = QLineEdit(self.widget_dados_cliente)
        self.line_celular_cliente.setObjectName(u"line_celular_cliente")

        self.layout_origanizador2.addWidget(self.line_celular_cliente)


        self.layout_organizador.addLayout(self.layout_origanizador2)


        self.verticalLayout_4.addLayout(self.layout_organizador)


        self.verticalLayout_3.addWidget(self.widget_dados_cliente)


        self.verticalLayout_16.addWidget(self.widget_ordem_servico)

        self.scrollArea.setWidget(self.layout_data)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.btn_gravar = QPushButton(self.create_order)
        self.btn_gravar.setObjectName(u"btn_gravar")
        self.btn_gravar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gravar.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	background-color:rgb(222, 221, 218);\n"
"	border-radius: 6px;\n"
"	color:rgb(36, 31, 49);\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(98, 160, 234);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_gravar)

        self.stackedWidget.addWidget(self.create_order)
        self.page_make = QWidget()
        self.page_make.setObjectName(u"page_make")
        self.verticalLayout_5 = QVBoxLayout(self.page_make)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.page_make)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 24px;")

        self.verticalLayout_5.addWidget(self.label_5)

        self.line_5 = QFrame(self.page_make)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.frame_make = QFrame(self.page_make)
        self.frame_make.setObjectName(u"frame_make")
        self.frame_make.setFrameShape(QFrame.StyledPanel)
        self.frame_make.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_make)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.frame_make)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 16px;")

        self.verticalLayout_17.addWidget(self.label_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.frame_make)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(36, 31, 49);")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.label_13 = QLabel(self.frame_make)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(36, 31, 49);")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.label_category_layout = QLabel(self.frame_make)
        self.label_category_layout.setObjectName(u"label_category_layout")
        self.label_category_layout.setStyleSheet(u"color: rgb(237, 51, 59);")

        self.horizontalLayout_14.addWidget(self.label_category_layout)


        self.verticalLayout_17.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.list_categoria = QListWidget(self.frame_make)
        self.list_categoria.setObjectName(u"list_categoria")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_categoria.sizePolicy().hasHeightForWidth())
        self.list_categoria.setSizePolicy(sizePolicy)
        self.list_categoria.setStyleSheet(u"color:black;")
        self.list_categoria.setSelectionMode(QAbstractItemView.MultiSelection)

        self.horizontalLayout_15.addWidget(self.list_categoria)

        self.table_categoria = QTableWidget(self.frame_make)
        if (self.table_categoria.columnCount() < 2):
            self.table_categoria.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_categoria.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_categoria.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_categoria.setObjectName(u"table_categoria")
        self.table_categoria.setStyleSheet(u"color:black;")
        self.table_categoria.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_categoria.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_categoria.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_categoria.horizontalHeader().setMinimumSectionSize(180)
        self.table_categoria.horizontalHeader().setStretchLastSection(True)
        self.table_categoria.verticalHeader().setDefaultSectionSize(50)

        self.horizontalLayout_15.addWidget(self.table_categoria)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_create_categoria = QPushButton(self.frame_make)
        self.btn_create_categoria.setObjectName(u"btn_create_categoria")
        self.btn_create_categoria.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	background-color: rgb(143, 240, 164);\n"
"	border-radius: 6px;\n"
"	color:black;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(51, 209, 122);\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_create_categoria)

        self.btn_edit_categoria = QPushButton(self.frame_make)
        self.btn_edit_categoria.setObjectName(u"btn_edit_categoria")
        self.btn_edit_categoria.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	\n"
"	background-color: rgb(249, 240, 107);\n"
"	border-radius: 6px;\n"
"	color:black;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(246, 211, 45);\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_edit_categoria)

        self.btn_pos_categoria = QPushButton(self.frame_make)
        self.btn_pos_categoria.setObjectName(u"btn_pos_categoria")
        self.btn_pos_categoria.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	\n"
"	background-color: rgb(246, 97, 81);\n"
"	border-radius: 6px;\n"
"	color:black;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(224, 27, 36);\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_pos_categoria)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.frame_make)

        self.stackedWidget.addWidget(self.page_make)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.verticalLayout_20 = QVBoxLayout(self.page_history)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_4 = QWidget(self.page_history)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"font-size: 24px;")

        self.verticalLayout_14.addWidget(self.label_7)

        self.line_6 = QFrame(self.widget_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_6)


        self.verticalLayout_20.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.page_history)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lineEdit_search = QLineEdit(self.widget_5)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setStyleSheet(u"height: 25px;\n"
"color: rgb(36, 31, 49);")

        self.verticalLayout_18.addWidget(self.lineEdit_search)


        self.horizontalLayout_8.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.radio_all = QRadioButton(self.widget_5)
        self.radio_all.setObjectName(u"radio_all")
        self.radio_all.setStyleSheet(u"color:black;")

        self.verticalLayout_19.addWidget(self.radio_all)

        self.radio_open = QRadioButton(self.widget_5)
        self.radio_open.setObjectName(u"radio_open")
        self.radio_open.setStyleSheet(u"color:black;")

        self.verticalLayout_19.addWidget(self.radio_open)

        self.radio_close = QRadioButton(self.widget_5)
        self.radio_close.setObjectName(u"radio_close")
        self.radio_close.setStyleSheet(u"color:black;")

        self.verticalLayout_19.addWidget(self.radio_close)


        self.horizontalLayout_8.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_20.addWidget(self.widget_5)

        self.table_history_order = QTableWidget(self.page_history)
        if (self.table_history_order.columnCount() < 4):
            self.table_history_order.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_history_order.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_history_order.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_history_order.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_history_order.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.table_history_order.setObjectName(u"table_history_order")
        self.table_history_order.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.table_history_order.setStyleSheet(u"QTableWidget{\n"
"	border:none;\n"
"}\n"
"QHeaderView::section { \n"
"padding: 10px;\n"
"border-radius: 6px;\n"
"margin-left: 3px;\n"
"margin-right: 3px;\n"
"color: rgb(36, 31, 49);\n"
"background-color: rgb(222, 221, 218);\n"
"\n"
"}\n"
"QTableWidget::item:hover {\n"
"	color: rgb(46, 52, 54);\n"
"}\n"
"QTableWidget::item {\n"
"	background-color: rgb(246, 245, 244);\n"
"	color: rgb(36, 31, 49);\n"
"	margin-top: 3px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QToolTip {\n"
"	color: white; \n"
"	background-color: rgb(165, 29, 45); \n"
"	border: 1px solid gray;\n"
" }")
        self.table_history_order.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_history_order.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_history_order.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_history_order.setTextElideMode(Qt.ElideLeft)
        self.table_history_order.setGridStyle(Qt.NoPen)
        self.table_history_order.horizontalHeader().setDefaultSectionSize(150)
        self.table_history_order.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_history_order.horizontalHeader().setStretchLastSection(True)
        self.table_history_order.verticalHeader().setVisible(False)
        self.table_history_order.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_20.addWidget(self.table_history_order)

        self.stackedWidget.addWidget(self.page_history)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 22))
        self.menuMENU_INCIIAL = QMenu(self.menubar)
        self.menuMENU_INCIIAL.setObjectName(u"menuMENU_INCIIAL")
        self.menuConfigura_o = QMenu(self.menubar)
        self.menuConfigura_o.setObjectName(u"menuConfigura_o")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMENU_INCIIAL.menuAction())
        self.menubar.addAction(self.menuConfigura_o.menuAction())
        self.menuMENU_INCIIAL.addAction(self.actionVoltar_para_tela_inicial)
        self.menuConfigura_o.addAction(self.actionLayout_Ordens)
        self.menuConfigura_o.addAction(self.actionVisualizar_Layout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionVoltar_para_tela_inicial.setText(QCoreApplication.translate("MainWindow", u"Voltar para tela inicial", None))
        self.actionLayout_Ordens.setText(QCoreApplication.translate("MainWindow", u"Layout Ordens", None))
        self.actionVisualizar_Layout.setText(QCoreApplication.translate("MainWindow", u"Visualizar Layout", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sistema de Ordem de Servi\u00e7o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ORDENS TOTAL", None))
        self.info_orders.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ORDENS EM ABERTO", None))
        self.info_orders_open.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ORDENS FINALIZADAS", None))
        self.info_orders_close.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ATALHOS", None))
        self.btn_r_o.setText(QCoreApplication.translate("MainWindow", u"NOVA ORDEM", None))
        self.btn_h_o.setText(QCoreApplication.translate("MainWindow", u"HISTORICO DE ORDENS", None))
        self.btn_e_o.setText(QCoreApplication.translate("MainWindow", u"EDI\u00c7\u00c3O DA ORDEM DE SERVI\u00c7O", None))
        self.btn__.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_ordem.setText(QCoreApplication.translate("MainWindow", u"ORDEM DE SERVI\u00c7O", None))
        self.label_data.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_dados_cliente.setText(QCoreApplication.translate("MainWindow", u"DADOS DO CLIENTE", None))
        self.btn_save_cliente.setText(QCoreApplication.translate("MainWindow", u"SALVAR CLIENTE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.btn_gravar.setText(QCoreApplication.translate("MainWindow", u"Registrar Ordem", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o da Ordem de Servi\u00e7o", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MENU DE CRIA\u00c7\u00c3O DE CATEGORIAS", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CATEGORIAS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CAMPOS DA CATEGORIA", None))
        self.label_category_layout.setText("")
        ___qtablewidgetitem = self.table_categoria.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME DO CAMPO", None));
        ___qtablewidgetitem1 = self.table_categoria.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TIPO DO CAMPO", None));
        self.btn_create_categoria.setText(QCoreApplication.translate("MainWindow", u"CRIAR NOVA CATEGORIA", None))
        self.btn_edit_categoria.setText(QCoreApplication.translate("MainWindow", u"EDITAR CATEGORIA", None))
        self.btn_pos_categoria.setText(QCoreApplication.translate("MainWindow", u"MUDAR POSI\u00c7\u00c3O DA CATEGORIA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"HISTORICO DE ORDENS", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.radio_all.setText(QCoreApplication.translate("MainWindow", u"Todos", None))
        self.radio_open.setText(QCoreApplication.translate("MainWindow", u"Abertas", None))
        self.radio_close.setText(QCoreApplication.translate("MainWindow", u"Finalizadas", None))
        ___qtablewidgetitem2 = self.table_history_order.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID ORDEM", None));
        ___qtablewidgetitem3 = self.table_history_order.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem4 = self.table_history_order.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem5 = self.table_history_order.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"DATA ORDEM", None));
        self.menuMENU_INCIIAL.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuConfigura_o.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
    # retranslateUi


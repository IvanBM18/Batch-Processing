# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 773)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"selection-color: rgb(255, 170, 255);\n"
"selection-background-color: rgb(255, 170, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(11, 11, 361, 691))
        self.groupBox.setStyleSheet(u"border-color: rgb(44, 47, 51);")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"selection-background-color: rgb(255, 170, 127);\n"
"border: 0px solid rgb(0, 153, 117);\n"
"")
        self.label_titulo = QLabel(self.groupBox_4)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(40, 10, 221, 31))
        self.label_titulo.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.textBox_Nombre = QLineEdit(self.groupBox_4)
        self.textBox_Nombre.setObjectName(u"textBox_Nombre")
        self.textBox_Nombre.setGeometry(QRect(110, 60, 144, 35))
        self.textBox_Nombre.setMinimumSize(QSize(60, 35))
        self.textBox_Nombre.setMaximumSize(QSize(230, 35))
        self.textBox_Nombre.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.textBox_numero1 = QLineEdit(self.groupBox_4)
        self.textBox_numero1.setObjectName(u"textBox_numero1")
        self.textBox_numero1.setGeometry(QRect(110, 110, 81, 35))
        self.textBox_numero1.setMinimumSize(QSize(60, 35))
        self.textBox_numero1.setMaximumSize(QSize(230, 35))
        self.textBox_numero1.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Nombre = QLabel(self.groupBox_4)
        self.label_Nombre.setObjectName(u"label_Nombre")
        self.label_Nombre.setGeometry(QRect(10, 60, 101, 31))
        self.label_Nombre.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.label_operacion = QLabel(self.groupBox_4)
        self.label_operacion.setObjectName(u"label_operacion")
        self.label_operacion.setGeometry(QRect(10, 110, 81, 31))
        self.label_operacion.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.comboBoxOperaciones = QComboBox(self.groupBox_4)
        self.comboBoxOperaciones.addItem("")
        self.comboBoxOperaciones.addItem("")
        self.comboBoxOperaciones.addItem("")
        self.comboBoxOperaciones.addItem("")
        self.comboBoxOperaciones.addItem("")
        self.comboBoxOperaciones.addItem("")
        self.comboBoxOperaciones.setObjectName(u"comboBoxOperaciones")
        self.comboBoxOperaciones.setGeometry(QRect(200, 110, 50, 35))
        self.comboBoxOperaciones.setMinimumSize(QSize(0, 35))
        self.comboBoxOperaciones.setMaximumSize(QSize(50, 35))
        self.comboBoxOperaciones.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 6px;\n"
"color: rgb(255, 255, 255);")
        self.textBox_numero2 = QLineEdit(self.groupBox_4)
        self.textBox_numero2.setObjectName(u"textBox_numero2")
        self.textBox_numero2.setGeometry(QRect(260, 110, 71, 35))
        self.textBox_numero2.setMinimumSize(QSize(60, 35))
        self.textBox_numero2.setMaximumSize(QSize(230, 35))
        self.textBox_numero2.setStyleSheet(u"border: 1px solid rgb(0, 153, 117);\n"
"background-color: rgb(52, 62, 64);\n"
"border-radius: 4px;")
        self.textBox_tiempo = QLineEdit(self.groupBox_4)
        self.textBox_tiempo.setObjectName(u"textBox_tiempo")
        self.textBox_tiempo.setGeometry(QRect(110, 160, 144, 35))
        self.textBox_tiempo.setMinimumSize(QSize(60, 35))
        self.textBox_tiempo.setMaximumSize(QSize(230, 35))
        self.textBox_tiempo.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_tiempo = QLabel(self.groupBox_4)
        self.label_tiempo.setObjectName(u"label_tiempo")
        self.label_tiempo.setGeometry(QRect(10, 160, 71, 31))
        self.label_tiempo.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_Id = QLineEdit(self.groupBox_4)
        self.textBox_Id.setObjectName(u"textBox_Id")
        self.textBox_Id.setGeometry(QRect(110, 220, 171, 35))
        self.textBox_Id.setMinimumSize(QSize(60, 35))
        self.textBox_Id.setMaximumSize(QSize(230, 35))
        self.textBox_Id.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 220, 31, 31))
        self.label_5.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.pushButton_Agregar = QPushButton(self.groupBox_4)
        self.pushButton_Agregar.setObjectName(u"pushButton_Agregar")
        self.pushButton_Agregar.setGeometry(QRect(30, 360, 111, 41))
        self.pushButton_Agregar.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"color: #FFFFFF;\n"
"font: 75 12pt \"Microsoft YaHei\";\n"
"border-radius: 10px;")
        self.pushButton_ejecturar = QPushButton(self.groupBox_4)
        self.pushButton_ejecturar.setObjectName(u"pushButton_ejecturar")
        self.pushButton_ejecturar.setGeometry(QRect(190, 360, 111, 41))
        self.pushButton_ejecturar.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"color: #FFFFFF;\n"
"font: 75 12pt \"Microsoft YaHei\";\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(378, 11, 360, 689))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 340, 321, 311))
        self.groupBox_5.setStyleSheet(u"selection-background-color: rgb(255, 170, 127);\n"
"border: 0px solid rgb(0, 153, 117);\n"
"")
        self.label_titulo_4 = QLabel(self.groupBox_5)
        self.label_titulo_4.setObjectName(u"label_titulo_4")
        self.label_titulo_4.setGeometry(QRect(80, 10, 221, 31))
        self.label_titulo_4.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_Nombre_proceso = QLineEdit(self.groupBox_5)
        self.textBox_Nombre_proceso.setObjectName(u"textBox_Nombre_proceso")
        self.textBox_Nombre_proceso.setGeometry(QRect(140, 60, 141, 35))
        self.textBox_Nombre_proceso.setMinimumSize(QSize(60, 35))
        self.textBox_Nombre_proceso.setMaximumSize(QSize(230, 35))
        self.textBox_Nombre_proceso.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.textBox_operacion = QLineEdit(self.groupBox_5)
        self.textBox_operacion.setObjectName(u"textBox_operacion")
        self.textBox_operacion.setGeometry(QRect(140, 110, 141, 35))
        self.textBox_operacion.setMinimumSize(QSize(60, 35))
        self.textBox_operacion.setMaximumSize(QSize(230, 35))
        self.textBox_operacion.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Nombre_4 = QLabel(self.groupBox_5)
        self.label_Nombre_4.setObjectName(u"label_Nombre_4")
        self.label_Nombre_4.setGeometry(QRect(10, 60, 91, 31))
        self.label_Nombre_4.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.label_operacion_4 = QLabel(self.groupBox_5)
        self.label_operacion_4.setObjectName(u"label_operacion_4")
        self.label_operacion_4.setGeometry(QRect(10, 110, 81, 31))
        self.label_operacion_4.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_tiempo_transcurrido = QLineEdit(self.groupBox_5)
        self.textBox_tiempo_transcurrido.setObjectName(u"textBox_tiempo_transcurrido")
        self.textBox_tiempo_transcurrido.setGeometry(QRect(140, 160, 141, 35))
        self.textBox_tiempo_transcurrido.setMinimumSize(QSize(60, 35))
        self.textBox_tiempo_transcurrido.setMaximumSize(QSize(230, 35))
        self.textBox_tiempo_transcurrido.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_tiempo_t = QLabel(self.groupBox_5)
        self.label_tiempo_t.setObjectName(u"label_tiempo_t")
        self.label_tiempo_t.setGeometry(QRect(10, 160, 101, 31))
        self.label_tiempo_t.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_Id_proceso = QLineEdit(self.groupBox_5)
        self.textBox_Id_proceso.setObjectName(u"textBox_Id_proceso")
        self.textBox_Id_proceso.setGeometry(QRect(140, 260, 141, 35))
        self.textBox_Id_proceso.setMinimumSize(QSize(60, 35))
        self.textBox_Id_proceso.setMaximumSize(QSize(230, 35))
        self.textBox_Id_proceso.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 260, 31, 31))
        self.label_8.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.label_tiempo_r = QLabel(self.groupBox_5)
        self.label_tiempo_r.setObjectName(u"label_tiempo_r")
        self.label_tiempo_r.setGeometry(QRect(10, 210, 101, 31))
        self.label_tiempo_r.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_tiempo_restante = QLineEdit(self.groupBox_5)
        self.textBox_tiempo_restante.setObjectName(u"textBox_tiempo_restante")
        self.textBox_tiempo_restante.setGeometry(QRect(140, 210, 144, 35))
        self.textBox_tiempo_restante.setMinimumSize(QSize(60, 35))
        self.textBox_tiempo_restante.setMaximumSize(QSize(230, 35))
        self.textBox_tiempo_restante.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.tablaProcesos = QTableWidget(self.groupBox_2)
        if (self.tablaProcesos.columnCount() < 4):
            self.tablaProcesos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablaProcesos.setObjectName(u"tablaProcesos")
        self.tablaProcesos.setGeometry(QRect(30, 100, 311, 181))
        self.tablaProcesos.setMinimumSize(QSize(305, 0))
        self.tablaProcesos.setMaximumSize(QSize(16777215, 250))
        self.tablaProcesos.setLayoutDirection(Qt.LeftToRight)
        self.tablaProcesos.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"")
        self.label_titulo_5 = QLabel(self.groupBox_2)
        self.label_titulo_5.setObjectName(u"label_titulo_5")
        self.label_titulo_5.setGeometry(QRect(30, 40, 121, 31))
        self.label_titulo_5.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.label_titulo_6 = QLabel(self.groupBox_2)
        self.label_titulo_6.setObjectName(u"label_titulo_6")
        self.label_titulo_6.setGeometry(QRect(190, 40, 101, 31))
        self.label_titulo_6.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_restantes = QLineEdit(self.groupBox_2)
        self.textBox_restantes.setObjectName(u"textBox_restantes")
        self.textBox_restantes.setGeometry(QRect(290, 40, 61, 35))
        self.textBox_restantes.setMinimumSize(QSize(60, 35))
        self.textBox_restantes.setMaximumSize(QSize(230, 35))
        self.textBox_restantes.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(745, 11, 531, 691))
        self.label_titulo_7 = QLabel(self.groupBox_3)
        self.label_titulo_7.setObjectName(u"label_titulo_7")
        self.label_titulo_7.setGeometry(QRect(110, 40, 221, 31))
        self.label_titulo_7.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.tablaPTerminados = QTableWidget(self.groupBox_3)
        if (self.tablaPTerminados.columnCount() < 4):
            self.tablaPTerminados.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tablaPTerminados.setObjectName(u"tablaPTerminados")
        self.tablaPTerminados.setGeometry(QRect(20, 100, 481, 451))
        self.tablaPTerminados.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"")
        self.label_titulo_8 = QLabel(self.groupBox_3)
        self.label_titulo_8.setObjectName(u"label_titulo_8")
        self.label_titulo_8.setGeometry(QRect(40, 590, 221, 31))
        self.label_titulo_8.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_contadorGlobal = QLineEdit(self.groupBox_3)
        self.textBox_contadorGlobal.setObjectName(u"textBox_contadorGlobal")
        self.textBox_contadorGlobal.setGeometry(QRect(170, 590, 71, 35))
        self.textBox_contadorGlobal.setMinimumSize(QSize(60, 35))
        self.textBox_contadorGlobal.setMaximumSize(QSize(230, 35))
        self.textBox_contadorGlobal.setStyleSheet(u"border: 1px solid rgb(0, 153, 117);\n"
"background-color: rgb(52, 62, 64);\n"
"border-radius: 4px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1260, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.groupBox_4.setTitle("")
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"Capturar procesos", None))
        self.textBox_Nombre.setText(QCoreApplication.translate("MainWindow", u"Ivan", None))
        self.label_Nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_operacion.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.comboBoxOperaciones.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.comboBoxOperaciones.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBoxOperaciones.setItemText(2, QCoreApplication.translate("MainWindow", u"*", None))
        self.comboBoxOperaciones.setItemText(3, QCoreApplication.translate("MainWindow", u"/", None))
        self.comboBoxOperaciones.setItemText(4, QCoreApplication.translate("MainWindow", u"%", None))
        self.comboBoxOperaciones.setItemText(5, QCoreApplication.translate("MainWindow", u"^", None))

        self.label_tiempo.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton_Agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pushButton_ejecturar.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.groupBox_2.setTitle("")
        self.groupBox_5.setTitle("")
        self.label_titulo_4.setText(QCoreApplication.translate("MainWindow", u"Proceso Actual", None))
        self.label_Nombre_4.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_operacion_4.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_tiempo_t.setText(QCoreApplication.translate("MainWindow", u"T. Transcurrido", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_tiempo_r.setText(QCoreApplication.translate("MainWindow", u"T. Restante", None))
        ___qtablewidgetitem = self.tablaProcesos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tablaProcesos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T. M\u00e1x", None));
        self.label_titulo_5.setText(QCoreApplication.translate("MainWindow", u"Lote Actual", None))
        self.label_titulo_6.setText(QCoreApplication.translate("MainWindow", u"Restantes", None))
        self.groupBox_3.setTitle("")
        self.label_titulo_7.setText(QCoreApplication.translate("MainWindow", u"Proceso Final", None))
        ___qtablewidgetitem2 = self.tablaPTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        ___qtablewidgetitem3 = self.tablaPTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.tablaPTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem5 = self.tablaPTerminados.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.label_titulo_8.setText(QCoreApplication.translate("MainWindow", u"Contador", None))
    # retranslateUi


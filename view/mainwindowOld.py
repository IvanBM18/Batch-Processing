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
        MainWindow.resize(1284, 756)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 50, 731, 521))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_process = QGroupBox(self.tab)
        self.groupBox_process.setObjectName(u"groupBox_process")
        self.label_process = QLabel(self.groupBox_process)
        self.label_process.setObjectName(u"label_process")
        self.label_process.setGeometry(QRect(10, 30, 74, 16))
        self.plainTextEdit_process = QPlainTextEdit(self.groupBox_process)
        self.plainTextEdit_process.setObjectName(u"plainTextEdit_process")
        self.plainTextEdit_process.setGeometry(QRect(90, 20, 454, 31))
        self.pushButton_aceptProcess = QPushButton(self.groupBox_process)
        self.pushButton_aceptProcess.setObjectName(u"pushButton_aceptProcess")
        self.pushButton_aceptProcess.setGeometry(QRect(560, 20, 93, 28))

        self.gridLayout.addWidget(self.groupBox_process, 0, 0, 1, 1)

        self.groupBox_name = QGroupBox(self.tab)
        self.groupBox_name.setObjectName(u"groupBox_name")
        self.plainTextEdit_name = QPlainTextEdit(self.groupBox_name)
        self.plainTextEdit_name.setObjectName(u"plainTextEdit_name")
        self.plainTextEdit_name.setGeometry(QRect(80, 30, 321, 31))
        self.label_name = QLabel(self.groupBox_name)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(20, 40, 51, 16))

        self.gridLayout.addWidget(self.groupBox_name, 1, 0, 1, 1)

        self.groupBox_operation = QGroupBox(self.tab)
        self.groupBox_operation.setObjectName(u"groupBox_operation")
        self.label_operacion = QLabel(self.groupBox_operation)
        self.label_operacion.setObjectName(u"label_operacion")
        self.label_operacion.setGeometry(QRect(10, 30, 71, 16))
        self.comboBox_operation = QComboBox(self.groupBox_operation)
        self.comboBox_operation.addItem("")
        self.comboBox_operation.addItem("")
        self.comboBox_operation.addItem("")
        self.comboBox_operation.addItem("")
        self.comboBox_operation.addItem("")
        self.comboBox_operation.addItem("")
        self.comboBox_operation.setObjectName(u"comboBox_operation")
        self.comboBox_operation.setGeometry(QRect(200, 20, 73, 21))
        self.plainTextEdit_operationFirst = QPlainTextEdit(self.groupBox_operation)
        self.plainTextEdit_operationFirst.setObjectName(u"plainTextEdit_operationFirst")
        self.plainTextEdit_operationFirst.setGeometry(QRect(100, 20, 61, 31))
        self.plainTextEdit_operationSecond = QPlainTextEdit(self.groupBox_operation)
        self.plainTextEdit_operationSecond.setObjectName(u"plainTextEdit_operationSecond")
        self.plainTextEdit_operationSecond.setGeometry(QRect(300, 20, 61, 31))

        self.gridLayout.addWidget(self.groupBox_operation, 2, 0, 1, 1)

        self.groupBox_operation_2 = QGroupBox(self.tab)
        self.groupBox_operation_2.setObjectName(u"groupBox_operation_2")
        self.label_time = QLabel(self.groupBox_operation_2)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(10, 30, 29, 16))
        self.plainTextEdit_SetTime = QPlainTextEdit(self.groupBox_operation_2)
        self.plainTextEdit_SetTime.setObjectName(u"plainTextEdit_SetTime")
        self.plainTextEdit_SetTime.setGeometry(QRect(48, 12, 256, 41))
        self.plainTextEdit_setID = QPlainTextEdit(self.groupBox_operation_2)
        self.plainTextEdit_setID.setObjectName(u"plainTextEdit_setID")
        self.plainTextEdit_setID.setGeometry(QRect(445, 10, 221, 41))
        self.label = QLabel(self.groupBox_operation_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 20, 54, 16))
        self.label_2 = QLabel(self.groupBox_operation_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 20, 16, 16))

        self.gridLayout.addWidget(self.groupBox_operation_2, 3, 0, 1, 1)

        self.groupBox_name_2 = QGroupBox(self.tab)
        self.groupBox_name_2.setObjectName(u"groupBox_name_2")
        self.label_name_2 = QLabel(self.groupBox_name_2)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setGeometry(QRect(10, 20, 55, 16))
        self.pushButton_addProcess = QPushButton(self.groupBox_name_2)
        self.pushButton_addProcess.setObjectName(u"pushButton_addProcess")
        self.pushButton_addProcess.setGeometry(QRect(20, 20, 93, 28))
        self.label_5 = QLabel(self.groupBox_name_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 30, 121, 20))
        self.plainTextEdit_capturedProcess = QPlainTextEdit(self.groupBox_name_2)
        self.plainTextEdit_capturedProcess.setObjectName(u"plainTextEdit_capturedProcess")
        self.plainTextEdit_capturedProcess.setGeometry(QRect(490, 20, 104, 31))

        self.gridLayout.addWidget(self.groupBox_name_2, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 20, 631, 101))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.plainTextEdit_PendingBatch = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_PendingBatch.setObjectName(u"plainTextEdit_PendingBatch")

        self.gridLayout_2.addWidget(self.plainTextEdit_PendingBatch, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.plainTextEdit_Counter = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Counter.setObjectName(u"plainTextEdit_Counter")

        self.gridLayout_2.addWidget(self.plainTextEdit_Counter, 0, 3, 2, 1)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 130, 321, 181))
        self.graphicsView = QGraphicsView(self.groupBox_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 60, 111, 111))
        self.graphicsView_3 = QGraphicsView(self.groupBox_2)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(180, 60, 111, 111))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 40, 60, 16))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 40, 60, 16))
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(410, 140, 261, 311))
        self.graphicsView_2 = QGraphicsView(self.groupBox_3)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(10, 20, 231, 281))
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(39, 330, 321, 131))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1284, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_process.setTitle("")
        self.label_process.setText(QCoreApplication.translate("MainWindow", u"No. Procesos", None))
        self.plainTextEdit_process.setPlainText("")
        self.pushButton_aceptProcess.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.groupBox_name.setTitle("")
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.groupBox_operation.setTitle("")
        self.label_operacion.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.comboBox_operation.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.comboBox_operation.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_operation.setItemText(2, QCoreApplication.translate("MainWindow", u"*", None))
        self.comboBox_operation.setItemText(3, QCoreApplication.translate("MainWindow", u"/", None))
        self.comboBox_operation.setItemText(4, QCoreApplication.translate("MainWindow", u"%", None))
        self.comboBox_operation.setItemText(5, QCoreApplication.translate("MainWindow", u"^", None))

        self.groupBox_operation_2.setTitle("")
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"segundos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.groupBox_name_2.setTitle("")
        self.label_name_2.setText("")
        self.pushButton_addProcess.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Procesos Capturados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Informacion del Proceso", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Simulador de procesamiento por lotes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"No. de Lotes pendientes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contador", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Lote en ejecucion", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Procesos", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Simulador ", None))
    # retranslateUi


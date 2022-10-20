# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1177, 788)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"selection-color: rgb(255, 170, 255);\n"
"selection-background-color: rgb(255, 170, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(11, 11, 271, 691))
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
        self.label_titulo.setGeometry(QRect(40, 40, 221, 31))
        self.label_titulo.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.textBox_NumProcess = QLineEdit(self.groupBox_4)
        self.textBox_NumProcess.setObjectName(u"textBox_NumProcess")
        self.textBox_NumProcess.setGeometry(QRect(0, 140, 230, 35))
        self.textBox_NumProcess.setMinimumSize(QSize(60, 35))
        self.textBox_NumProcess.setMaximumSize(QSize(230, 35))
        self.textBox_NumProcess.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Numero = QLabel(self.groupBox_4)
        self.label_Numero.setObjectName(u"label_Numero")
        self.label_Numero.setGeometry(QRect(20, 110, 171, 21))
        self.label_Numero.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.pushButton_Agregar = QPushButton(self.groupBox_4)
        self.pushButton_Agregar.setObjectName(u"pushButton_Agregar")
        self.pushButton_Agregar.setGeometry(QRect(30, 300, 111, 41))
        self.pushButton_Agregar.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"color: #FFFFFF;\n"
"font: 75 12pt \"Microsoft YaHei\";\n"
"border-radius: 10px;")
        self.pushButton_Ejecutar = QPushButton(self.groupBox_4)
        self.pushButton_Ejecutar.setObjectName(u"pushButton_Ejecutar")
        self.pushButton_Ejecutar.setGeometry(QRect(150, 300, 111, 41))
        self.pushButton_Ejecutar.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"color: #FFFFFF;\n"
"font: 75 12pt \"Microsoft YaHei\";\n"
"border-radius: 10px;")
        self.tablaPbloqueados = QTableWidget(self.groupBox_4)
        if (self.tablaPbloqueados.columnCount() < 2):
            self.tablaPbloqueados.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaPbloqueados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaPbloqueados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tablaPbloqueados.setObjectName(u"tablaPbloqueados")
        self.tablaPbloqueados.setEnabled(False)
        self.tablaPbloqueados.setGeometry(QRect(20, 380, 211, 251))
        self.tablaPbloqueados.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPbloqueados.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPbloqueados.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPbloqueados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPbloqueados.horizontalHeader().setDefaultSectionSize(104)
        self.tablaPbloqueados.verticalHeader().setVisible(False)
        self.label_titulo_ProceL_2 = QLabel(self.groupBox_4)
        self.label_titulo_ProceL_2.setObjectName(u"label_titulo_ProceL_2")
        self.label_titulo_ProceL_2.setGeometry(QRect(40, 340, 171, 31))
        self.label_titulo_ProceL_2.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_NumProcess_2 = QLineEdit(self.groupBox_4)
        self.textBox_NumProcess_2.setObjectName(u"textBox_NumProcess_2")
        self.textBox_NumProcess_2.setGeometry(QRect(0, 230, 230, 35))
        self.textBox_NumProcess_2.setMinimumSize(QSize(60, 35))
        self.textBox_NumProcess_2.setMaximumSize(QSize(230, 35))
        self.textBox_NumProcess_2.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Numero_2 = QLabel(self.groupBox_4)
        self.label_Numero_2.setObjectName(u"label_Numero_2")
        self.label_Numero_2.setGeometry(QRect(10, 200, 171, 21))
        self.label_Numero_2.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")

        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QRect(290, 10, 360, 689))
        self.groupBox_2.setSizeIncrement(QSize(6, 6))
        self.groupBox_2.setBaseSize(QSize(9, 6))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 300, 321, 361))
        self.groupBox_5.setBaseSize(QSize(7, 7))
        self.groupBox_5.setStyleSheet(u"selection-background-color: rgb(255, 170, 127);\n"
"border: 0px solid rgb(0, 153, 117);\n"
"")
        self.label_titulo_procesoEje = QLabel(self.groupBox_5)
        self.label_titulo_procesoEje.setObjectName(u"label_titulo_procesoEje")
        self.label_titulo_procesoEje.setGeometry(QRect(60, 40, 221, 31))
        self.label_titulo_procesoEje.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_operacion = QLineEdit(self.groupBox_5)
        self.textBox_operacion.setObjectName(u"textBox_operacion")
        self.textBox_operacion.setGeometry(QRect(140, 110, 141, 35))
        self.textBox_operacion.setMinimumSize(QSize(60, 35))
        self.textBox_operacion.setMaximumSize(QSize(230, 35))
        self.textBox_operacion.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
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
        self.label_tiempo_t.setGeometry(QRect(10, 160, 111, 31))
        self.label_tiempo_t.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_Id_proceso = QLineEdit(self.groupBox_5)
        self.textBox_Id_proceso.setObjectName(u"textBox_Id_proceso")
        self.textBox_Id_proceso.setGeometry(QRect(140, 310, 141, 35))
        self.textBox_Id_proceso.setMinimumSize(QSize(60, 35))
        self.textBox_Id_proceso.setMaximumSize(QSize(230, 35))
        self.textBox_Id_proceso.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
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
        self.textBox_quantum = QLineEdit(self.groupBox_5)
        self.textBox_quantum.setObjectName(u"textBox_quantum")
        self.textBox_quantum.setGeometry(QRect(140, 260, 144, 35))
        self.textBox_quantum.setMinimumSize(QSize(60, 35))
        self.textBox_quantum.setMaximumSize(QSize(230, 35))
        self.textBox_quantum.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_id = QLabel(self.groupBox_5)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setGeometry(QRect(20, 310, 31, 31))
        self.label_id.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.label_id_2 = QLabel(self.groupBox_5)
        self.label_id_2.setObjectName(u"label_id_2")
        self.label_id_2.setGeometry(QRect(10, 260, 71, 31))
        self.label_id_2.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.tablaProcesos = QTableWidget(self.groupBox_2)
        if (self.tablaProcesos.columnCount() < 3):
            self.tablaProcesos.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tablaProcesos.setObjectName(u"tablaProcesos")
        self.tablaProcesos.setEnabled(False)
        self.tablaProcesos.setGeometry(QRect(20, 60, 315, 203))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(21)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.tablaProcesos.sizePolicy().hasHeightForWidth())
        self.tablaProcesos.setSizePolicy(sizePolicy)
        self.tablaProcesos.setSizeIncrement(QSize(7, 0))
        self.tablaProcesos.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tablaProcesos.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tablaProcesos.setAcceptDrops(True)
        self.tablaProcesos.setLayoutDirection(Qt.LeftToRight)
        self.tablaProcesos.setAutoFillBackground(True)
        self.tablaProcesos.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"")
        self.tablaProcesos.setFrameShape(QFrame.StyledPanel)
        self.tablaProcesos.setFrameShadow(QFrame.Raised)
        self.tablaProcesos.setLineWidth(4)
        self.tablaProcesos.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablaProcesos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaProcesos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaProcesos.setAutoScroll(True)
        self.tablaProcesos.setTabKeyNavigation(False)
        self.tablaProcesos.setProperty("showDropIndicator", False)
        self.tablaProcesos.setDragEnabled(False)
        self.tablaProcesos.setDragDropOverwriteMode(False)
        self.tablaProcesos.setGridStyle(Qt.NoPen)
        self.tablaProcesos.setSortingEnabled(False)
        self.tablaProcesos.setWordWrap(True)
        self.tablaProcesos.setCornerButtonEnabled(False)
        self.tablaProcesos.setRowCount(0)
        self.tablaProcesos.horizontalHeader().setVisible(True)
        self.tablaProcesos.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaProcesos.horizontalHeader().setMinimumSectionSize(35)
        self.tablaProcesos.horizontalHeader().setDefaultSectionSize(104)
        self.tablaProcesos.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaProcesos.horizontalHeader().setStretchLastSection(False)
        self.tablaProcesos.verticalHeader().setVisible(False)
        self.tablaProcesos.verticalHeader().setCascadingSectionResizes(True)
        self.tablaProcesos.verticalHeader().setMinimumSectionSize(34)
        self.tablaProcesos.verticalHeader().setDefaultSectionSize(34)
        self.tablaProcesos.verticalHeader().setHighlightSections(False)
        self.label_titulo_ProceL = QLabel(self.groupBox_2)
        self.label_titulo_ProceL.setObjectName(u"label_titulo_ProceL")
        self.label_titulo_ProceL.setGeometry(QRect(110, 20, 131, 31))
        self.label_titulo_ProceL.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.label_titulo_Nuevos = QLabel(self.groupBox_2)
        self.label_titulo_Nuevos.setObjectName(u"label_titulo_Nuevos")
        self.label_titulo_Nuevos.setGeometry(QRect(90, 270, 81, 31))
        self.label_titulo_Nuevos.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_restantes = QLineEdit(self.groupBox_2)
        self.textBox_restantes.setObjectName(u"textBox_restantes")
        self.textBox_restantes.setGeometry(QRect(180, 270, 61, 35))
        self.textBox_restantes.setMinimumSize(QSize(60, 35))
        self.textBox_restantes.setMaximumSize(QSize(230, 35))
        self.textBox_restantes.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(660, 10, 531, 691))
        self.label_titulo_ProcesoT = QLabel(self.groupBox_3)
        self.label_titulo_ProcesoT.setObjectName(u"label_titulo_ProcesoT")
        self.label_titulo_ProcesoT.setGeometry(QRect(190, 50, 221, 31))
        self.label_titulo_ProcesoT.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.tablaPTerminados = QTableWidget(self.groupBox_3)
        if (self.tablaPTerminados.columnCount() < 3):
            self.tablaPTerminados.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.tablaPTerminados.setObjectName(u"tablaPTerminados")
        self.tablaPTerminados.setEnabled(False)
        self.tablaPTerminados.setGeometry(QRect(120, 80, 301, 491))
        self.tablaPTerminados.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPTerminados.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablaPTerminados.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPTerminados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPTerminados.setAutoScroll(False)
        self.tablaPTerminados.horizontalHeader().setDefaultSectionSize(104)
        self.tablaPTerminados.verticalHeader().setVisible(False)
        self.label_titulo_Cont = QLabel(self.groupBox_3)
        self.label_titulo_Cont.setObjectName(u"label_titulo_Cont")
        self.label_titulo_Cont.setGeometry(QRect(290, 630, 101, 31))
        self.label_titulo_Cont.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_contadorGlobal = QLineEdit(self.groupBox_3)
        self.textBox_contadorGlobal.setObjectName(u"textBox_contadorGlobal")
        self.textBox_contadorGlobal.setGeometry(QRect(370, 630, 71, 35))
        self.textBox_contadorGlobal.setMinimumSize(QSize(60, 35))
        self.textBox_contadorGlobal.setMaximumSize(QSize(230, 35))
        self.textBox_contadorGlobal.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.textBox_quantumGlobal = QLineEdit(self.groupBox_3)
        self.textBox_quantumGlobal.setObjectName(u"textBox_quantumGlobal")
        self.textBox_quantumGlobal.setGeometry(QRect(110, 630, 71, 35))
        self.textBox_quantumGlobal.setMinimumSize(QSize(60, 35))
        self.textBox_quantumGlobal.setMaximumSize(QSize(230, 35))
        self.textBox_quantumGlobal.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_titulo_Cont_2 = QLabel(self.groupBox_3)
        self.label_titulo_Cont_2.setObjectName(u"label_titulo_Cont_2")
        self.label_titulo_Cont_2.setGeometry(QRect(20, 630, 101, 31))
        self.label_titulo_Cont_2.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1177, 22))
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
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"Capturar inicial", None))
        self.textBox_NumProcess.setText("")
        self.label_Numero.setText(QCoreApplication.translate("MainWindow", u"Numero de procesos", None))
        self.pushButton_Agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pushButton_Ejecutar.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        ___qtablewidgetitem = self.tablaPbloqueados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tablaPbloqueados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T. Bloqueo", None));
        self.label_titulo_ProceL_2.setText(QCoreApplication.translate("MainWindow", u"Procesos Bloqueados", None))
        self.textBox_NumProcess_2.setText("")
        self.label_Numero_2.setText(QCoreApplication.translate("MainWindow", u"Quantum ", None))
        self.groupBox_2.setTitle("")
        self.groupBox_5.setTitle("")
        self.label_titulo_procesoEje.setText(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        self.label_operacion_4.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_tiempo_t.setText(QCoreApplication.translate("MainWindow", u"T. Transcurrido", None))
        self.label_tiempo_r.setText(QCoreApplication.translate("MainWindow", u"T. Restante", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_id_2.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
        ___qtablewidgetitem2 = self.tablaProcesos.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.tablaProcesos.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T. M\u00e1x", None));
        ___qtablewidgetitem4 = self.tablaProcesos.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T. Transcurrido", None));
        self.label_titulo_ProceL.setText(QCoreApplication.translate("MainWindow", u"Procesos listos", None))
        self.label_titulo_Nuevos.setText(QCoreApplication.translate("MainWindow", u"Nuevos:", None))
        self.groupBox_3.setTitle("")
        self.label_titulo_ProcesoT.setText(QCoreApplication.translate("MainWindow", u"Procesos Terminados", None))
        ___qtablewidgetitem5 = self.tablaPTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tablaPTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem7 = self.tablaPTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.label_titulo_Cont.setText(QCoreApplication.translate("MainWindow", u"Contador", None))
        self.textBox_contadorGlobal.setText("")
        self.textBox_quantumGlobal.setText("")
        self.label_titulo_Cont_2.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1510, 674)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"selection-color: rgb(255, 170, 255);\n"
"selection-background-color: rgb(255, 170, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 271, 641))
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
        self.textBox_NumProcess.setGeometry(QRect(0, 110, 230, 35))
        self.textBox_NumProcess.setMinimumSize(QSize(60, 35))
        self.textBox_NumProcess.setMaximumSize(QSize(230, 35))
        self.textBox_NumProcess.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Numero = QLabel(self.groupBox_4)
        self.label_Numero.setObjectName(u"label_Numero")
        self.label_Numero.setGeometry(QRect(10, 80, 171, 21))
        self.label_Numero.setAutoFillBackground(False)
        self.label_Numero.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.pushButton_Agregar = QPushButton(self.groupBox_4)
        self.pushButton_Agregar.setObjectName(u"pushButton_Agregar")
        self.pushButton_Agregar.setGeometry(QRect(0, 250, 121, 41))
        self.pushButton_Agregar.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"color: #FFFFFF;\n"
"font: 75 12pt \"Microsoft YaHei\";\n"
"border-radius: 10px;")
        self.pushButton_Ejecutar = QPushButton(self.groupBox_4)
        self.pushButton_Ejecutar.setObjectName(u"pushButton_Ejecutar")
        self.pushButton_Ejecutar.setGeometry(QRect(130, 250, 111, 41))
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
        self.tablaPbloqueados.setGeometry(QRect(20, 350, 211, 251))
        self.tablaPbloqueados.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPbloqueados.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPbloqueados.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPbloqueados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPbloqueados.horizontalHeader().setDefaultSectionSize(104)
        self.tablaPbloqueados.verticalHeader().setVisible(False)
        self.label_titulo_ProceL_2 = QLabel(self.groupBox_4)
        self.label_titulo_ProceL_2.setObjectName(u"label_titulo_ProceL_2")
        self.label_titulo_ProceL_2.setGeometry(QRect(40, 310, 171, 31))
        self.label_titulo_ProceL_2.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_Quantum = QLineEdit(self.groupBox_4)
        self.textBox_Quantum.setObjectName(u"textBox_Quantum")
        self.textBox_Quantum.setGeometry(QRect(0, 190, 230, 35))
        self.textBox_Quantum.setMinimumSize(QSize(60, 35))
        self.textBox_Quantum.setMaximumSize(QSize(230, 35))
        self.textBox_Quantum.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Numero_2 = QLabel(self.groupBox_4)
        self.label_Numero_2.setObjectName(u"label_Numero_2")
        self.label_Numero_2.setGeometry(QRect(10, 160, 171, 21))
        self.label_Numero_2.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")

        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QRect(279, 10, 371, 641))
        self.groupBox_2.setSizeIncrement(QSize(6, 6))
        self.groupBox_2.setBaseSize(QSize(9, 6))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 260, 321, 341))
        self.groupBox_5.setBaseSize(QSize(7, 7))
        self.groupBox_5.setStyleSheet(u"selection-background-color: rgb(255, 170, 127);\n"
"border: 0px solid rgb(0, 153, 117);\n"
"")
        self.label_titulo_procesoEje = QLabel(self.groupBox_5)
        self.label_titulo_procesoEje.setObjectName(u"label_titulo_procesoEje")
        self.label_titulo_procesoEje.setGeometry(QRect(90, 90, 221, 31))
        self.label_titulo_procesoEje.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_operacion = QLineEdit(self.groupBox_5)
        self.textBox_operacion.setObjectName(u"textBox_operacion")
        self.textBox_operacion.setGeometry(QRect(150, 120, 141, 35))
        self.textBox_operacion.setMinimumSize(QSize(60, 35))
        self.textBox_operacion.setMaximumSize(QSize(230, 35))
        self.textBox_operacion.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_operacion_4 = QLabel(self.groupBox_5)
        self.label_operacion_4.setObjectName(u"label_operacion_4")
        self.label_operacion_4.setGeometry(QRect(20, 120, 81, 31))
        self.label_operacion_4.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_tiempo_transcurrido = QLineEdit(self.groupBox_5)
        self.textBox_tiempo_transcurrido.setObjectName(u"textBox_tiempo_transcurrido")
        self.textBox_tiempo_transcurrido.setGeometry(QRect(150, 160, 141, 35))
        self.textBox_tiempo_transcurrido.setMinimumSize(QSize(60, 35))
        self.textBox_tiempo_transcurrido.setMaximumSize(QSize(230, 35))
        self.textBox_tiempo_transcurrido.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_tiempo_t = QLabel(self.groupBox_5)
        self.label_tiempo_t.setObjectName(u"label_tiempo_t")
        self.label_tiempo_t.setGeometry(QRect(20, 160, 111, 31))
        self.label_tiempo_t.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_Id_proceso = QLineEdit(self.groupBox_5)
        self.textBox_Id_proceso.setObjectName(u"textBox_Id_proceso")
        self.textBox_Id_proceso.setGeometry(QRect(150, 240, 141, 35))
        self.textBox_Id_proceso.setMinimumSize(QSize(60, 35))
        self.textBox_Id_proceso.setMaximumSize(QSize(230, 35))
        self.textBox_Id_proceso.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_tiempo_r = QLabel(self.groupBox_5)
        self.label_tiempo_r.setObjectName(u"label_tiempo_r")
        self.label_tiempo_r.setGeometry(QRect(20, 200, 101, 31))
        self.label_tiempo_r.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_tiempo_restante = QLineEdit(self.groupBox_5)
        self.textBox_tiempo_restante.setObjectName(u"textBox_tiempo_restante")
        self.textBox_tiempo_restante.setGeometry(QRect(150, 200, 141, 35))
        self.textBox_tiempo_restante.setMinimumSize(QSize(60, 35))
        self.textBox_tiempo_restante.setMaximumSize(QSize(230, 35))
        self.textBox_tiempo_restante.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_id = QLabel(self.groupBox_5)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setGeometry(QRect(20, 240, 31, 31))
        self.label_id.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_proximo_size = QLineEdit(self.groupBox_5)
        self.textBox_proximo_size.setObjectName(u"textBox_proximo_size")
        self.textBox_proximo_size.setGeometry(QRect(230, 50, 61, 35))
        self.textBox_proximo_size.setMinimumSize(QSize(60, 35))
        self.textBox_proximo_size.setMaximumSize(QSize(230, 35))
        self.textBox_proximo_size.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.textBox_proximo_id = QLineEdit(self.groupBox_5)
        self.textBox_proximo_id.setObjectName(u"textBox_proximo_id")
        self.textBox_proximo_id.setGeometry(QRect(90, 50, 61, 35))
        self.textBox_proximo_id.setMinimumSize(QSize(60, 35))
        self.textBox_proximo_id.setMaximumSize(QSize(230, 35))
        self.textBox_proximo_id.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_titulo_Nuevos_2 = QLabel(self.groupBox_5)
        self.label_titulo_Nuevos_2.setObjectName(u"label_titulo_Nuevos_2")
        self.label_titulo_Nuevos_2.setGeometry(QRect(80, 10, 151, 31))
        self.label_titulo_Nuevos_2.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.label_Numero_tamanio = QLabel(self.groupBox_5)
        self.label_Numero_tamanio.setObjectName(u"label_Numero_tamanio")
        self.label_Numero_tamanio.setGeometry(QRect(170, 60, 51, 21))
        self.label_Numero_tamanio.setAutoFillBackground(True)
        self.label_Numero_tamanio.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.label_Numero_id = QLabel(self.groupBox_5)
        self.label_Numero_id.setObjectName(u"label_Numero_id")
        self.label_Numero_id.setGeometry(QRect(50, 60, 21, 21))
        self.label_Numero_id.setAutoFillBackground(False)
        self.label_Numero_id.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.textBox_Id_quantum = QLineEdit(self.groupBox_5)
        self.textBox_Id_quantum.setObjectName(u"textBox_Id_quantum")
        self.textBox_Id_quantum.setGeometry(QRect(150, 280, 141, 35))
        self.textBox_Id_quantum.setMinimumSize(QSize(60, 35))
        self.textBox_Id_quantum.setMaximumSize(QSize(230, 35))
        self.textBox_Id_quantum.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_id_quantum = QLabel(self.groupBox_5)
        self.label_id_quantum.setObjectName(u"label_id_quantum")
        self.label_id_quantum.setGeometry(QRect(20, 280, 61, 31))
        self.label_id_quantum.setStyleSheet(u"color:rgb(255, 255, 255);\n"
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
        self.tablaProcesos.setGeometry(QRect(20, 60, 315, 181))
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
        self.label_titulo_ProceL.setGeometry(QRect(20, 20, 131, 31))
        self.label_titulo_ProceL.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.label_titulo_Nuevos = QLabel(self.groupBox_2)
        self.label_titulo_Nuevos.setObjectName(u"label_titulo_Nuevos")
        self.label_titulo_Nuevos.setGeometry(QRect(210, 10, 61, 31))
        self.label_titulo_Nuevos.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_restantes = QLineEdit(self.groupBox_2)
        self.textBox_restantes.setObjectName(u"textBox_restantes")
        self.textBox_restantes.setGeometry(QRect(280, 10, 61, 35))
        self.textBox_restantes.setMinimumSize(QSize(60, 35))
        self.textBox_restantes.setMaximumSize(QSize(230, 35))
        self.textBox_restantes.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(630, 10, 401, 641))
        self.label_titulo_ProcesoT = QLabel(self.groupBox_3)
        self.label_titulo_ProcesoT.setObjectName(u"label_titulo_ProcesoT")
        self.label_titulo_ProcesoT.setGeometry(QRect(70, 20, 221, 31))
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
        self.tablaPTerminados.setGeometry(QRect(40, 60, 301, 491))
        self.tablaPTerminados.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPTerminados.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablaPTerminados.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPTerminados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPTerminados.setAutoScroll(False)
        self.tablaPTerminados.setDragEnabled(False)
        self.tablaPTerminados.setAlternatingRowColors(False)
        self.tablaPTerminados.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaPTerminados.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaPTerminados.horizontalHeader().setDefaultSectionSize(104)
        self.tablaPTerminados.verticalHeader().setVisible(False)
        self.label_titulo_Cont = QLabel(self.groupBox_3)
        self.label_titulo_Cont.setObjectName(u"label_titulo_Cont")
        self.label_titulo_Cont.setGeometry(QRect(230, 580, 101, 31))
        self.label_titulo_Cont.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_contadorGlobal = QLineEdit(self.groupBox_3)
        self.textBox_contadorGlobal.setObjectName(u"textBox_contadorGlobal")
        self.textBox_contadorGlobal.setGeometry(QRect(320, 580, 71, 35))
        self.textBox_contadorGlobal.setMinimumSize(QSize(60, 35))
        self.textBox_contadorGlobal.setMaximumSize(QSize(230, 35))
        self.textBox_contadorGlobal.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.textBox_quantumGlobal = QLineEdit(self.groupBox_3)
        self.textBox_quantumGlobal.setObjectName(u"textBox_quantumGlobal")
        self.textBox_quantumGlobal.setGeometry(QRect(130, 580, 71, 35))
        self.textBox_quantumGlobal.setMinimumSize(QSize(60, 35))
        self.textBox_quantumGlobal.setMaximumSize(QSize(230, 35))
        self.textBox_quantumGlobal.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_titulo_quatum = QLabel(self.groupBox_3)
        self.label_titulo_quatum.setObjectName(u"label_titulo_quatum")
        self.label_titulo_quatum.setGeometry(QRect(30, 580, 91, 31))
        self.label_titulo_quatum.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(1030, 10, 471, 641))
        self.label_titulo_ProcesoTableP = QLabel(self.groupBox_6)
        self.label_titulo_ProcesoTableP.setObjectName(u"label_titulo_ProcesoTableP")
        self.label_titulo_ProcesoTableP.setGeometry(QRect(170, 40, 131, 31))
        self.label_titulo_ProcesoTableP.setAutoFillBackground(False)
        self.label_titulo_ProcesoTableP.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(40, 100, 421, 491))
        self.tablaPaginacionL = QTableWidget(self.groupBox_7)
        if (self.tablaPaginacionL.columnCount() < 3):
            self.tablaPaginacionL.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setText(u"ID");
        __qtablewidgetitem8.setBackground(QColor(0, 2, 0));
        self.tablaPaginacionL.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaPaginacionL.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaPaginacionL.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.tablaPaginacionL.rowCount() < 22):
            self.tablaPaginacionL.setRowCount(22)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(10, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(11, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(12, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(13, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(14, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(15, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(16, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(17, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(18, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(19, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(20, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tablaPaginacionL.setVerticalHeaderItem(21, __qtablewidgetitem32)
        brush = QBrush(QColor(85, 255, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(255, 170, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setBackground(brush1);
        __qtablewidgetitem33.setForeground(brush);
        __qtablewidgetitem33.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tablaPaginacionL.setItem(0, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(0, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(1, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(2, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(3, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(4, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(5, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(6, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(7, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(8, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(9, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(10, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(11, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(12, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(12, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(13, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(13, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(14, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(15, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(16, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(17, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(18, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(19, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(20, 1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tablaPaginacionL.setItem(21, 1, __qtablewidgetitem57)
        self.tablaPaginacionL.setObjectName(u"tablaPaginacionL")
        self.tablaPaginacionL.setEnabled(False)
        self.tablaPaginacionL.setGeometry(QRect(20, 10, 171, 471))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tablaPaginacionL.sizePolicy().hasHeightForWidth())
        self.tablaPaginacionL.setSizePolicy(sizePolicy1)
#if QT_CONFIG(accessibility)
        self.tablaPaginacionL.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.tablaPaginacionL.setAutoFillBackground(False)
        self.tablaPaginacionL.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPaginacionL.setFrameShape(QFrame.StyledPanel)
        self.tablaPaginacionL.setFrameShadow(QFrame.Sunken)
        self.tablaPaginacionL.setLineWidth(0)
        self.tablaPaginacionL.setMidLineWidth(0)
        self.tablaPaginacionL.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablaPaginacionL.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPaginacionL.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPaginacionL.setAutoScroll(True)
        self.tablaPaginacionL.setTabKeyNavigation(False)
        self.tablaPaginacionL.setDragEnabled(False)
        self.tablaPaginacionL.setAlternatingRowColors(False)
        self.tablaPaginacionL.setIconSize(QSize(8, 10))
        self.tablaPaginacionL.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaPaginacionL.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaPaginacionL.setShowGrid(True)
        self.tablaPaginacionL.setWordWrap(False)
        self.tablaPaginacionL.setCornerButtonEnabled(False)
        self.tablaPaginacionL.horizontalHeader().setMinimumSectionSize(16)
        self.tablaPaginacionL.horizontalHeader().setDefaultSectionSize(55)
        self.tablaPaginacionL.verticalHeader().setVisible(False)
        self.tablaPaginacionL.verticalHeader().setMinimumSectionSize(0)
        self.tablaPaginacionL.verticalHeader().setDefaultSectionSize(20)
        self.tablaPaginacionL.verticalHeader().setProperty("showSortIndicator", True)
        self.tablaPaginacionL.verticalHeader().setStretchLastSection(False)
        self.tablaPaginacionR = QTableWidget(self.groupBox_7)
        if (self.tablaPaginacionR.columnCount() < 3):
            self.tablaPaginacionR.setColumnCount(3)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setText(u"ID");
        __qtablewidgetitem58.setBackground(QColor(0, 2, 0));
        self.tablaPaginacionR.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tablaPaginacionR.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tablaPaginacionR.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        if (self.tablaPaginacionR.rowCount() < 22):
            self.tablaPaginacionR.setRowCount(22)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(5, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(6, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(7, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(8, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(9, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(10, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(11, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(12, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(13, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(14, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(15, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(16, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(17, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(18, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(19, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(20, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tablaPaginacionR.setVerticalHeaderItem(21, __qtablewidgetitem82)
        brush2 = QBrush(QColor(85, 255, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(255, 170, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem83.setBackground(brush3);
        __qtablewidgetitem83.setForeground(brush2);
        __qtablewidgetitem83.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tablaPaginacionR.setItem(0, 0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(0, 1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(1, 1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(2, 1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(3, 1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(4, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(5, 1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(6, 1, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(7, 1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(8, 1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(9, 1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(10, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(11, 1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(12, 0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(12, 1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(13, 0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(13, 1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(14, 1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(15, 1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(16, 1, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(17, 1, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(18, 1, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(19, 1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(20, 1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tablaPaginacionR.setItem(21, 1, __qtablewidgetitem107)
        self.tablaPaginacionR.setObjectName(u"tablaPaginacionR")
        self.tablaPaginacionR.setEnabled(False)
        self.tablaPaginacionR.setGeometry(QRect(230, 10, 171, 471))
        sizePolicy1.setHeightForWidth(self.tablaPaginacionR.sizePolicy().hasHeightForWidth())
        self.tablaPaginacionR.setSizePolicy(sizePolicy1)
#if QT_CONFIG(accessibility)
        self.tablaPaginacionR.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.tablaPaginacionR.setAutoFillBackground(False)
        self.tablaPaginacionR.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPaginacionR.setFrameShape(QFrame.StyledPanel)
        self.tablaPaginacionR.setFrameShadow(QFrame.Sunken)
        self.tablaPaginacionR.setLineWidth(0)
        self.tablaPaginacionR.setMidLineWidth(0)
        self.tablaPaginacionR.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablaPaginacionR.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablaPaginacionR.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPaginacionR.setAutoScroll(True)
        self.tablaPaginacionR.setTabKeyNavigation(False)
        self.tablaPaginacionR.setDragEnabled(False)
        self.tablaPaginacionR.setAlternatingRowColors(False)
        self.tablaPaginacionR.setIconSize(QSize(8, 10))
        self.tablaPaginacionR.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaPaginacionR.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaPaginacionR.setShowGrid(True)
        self.tablaPaginacionR.setWordWrap(False)
        self.tablaPaginacionR.setCornerButtonEnabled(False)
        self.tablaPaginacionR.horizontalHeader().setMinimumSectionSize(16)
        self.tablaPaginacionR.horizontalHeader().setDefaultSectionSize(55)
        self.tablaPaginacionR.verticalHeader().setVisible(False)
        self.tablaPaginacionR.verticalHeader().setMinimumSectionSize(0)
        self.tablaPaginacionR.verticalHeader().setDefaultSectionSize(20)
        self.tablaPaginacionR.verticalHeader().setProperty("showSortIndicator", True)
        self.tablaPaginacionR.verticalHeader().setStretchLastSection(False)
        self.progressBar = QProgressBar(self.groupBox_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(130, 40, 51, 16))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(False)
        self.progressBar_1 = QProgressBar(self.groupBox_7)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setGeometry(QRect(340, 40, 51, 16))
        self.progressBar_1.setAutoFillBackground(False)
        self.progressBar_1.setValue(100)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_2 = QProgressBar(self.groupBox_7)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(130, 60, 51, 16))
        self.progressBar_2.setAutoFillBackground(False)
        self.progressBar_2.setValue(100)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_3 = QProgressBar(self.groupBox_7)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(340, 60, 51, 16))
        self.progressBar_3.setAutoFillBackground(False)
        self.progressBar_3.setValue(100)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_4 = QProgressBar(self.groupBox_7)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setGeometry(QRect(130, 80, 51, 16))
        self.progressBar_4.setAutoFillBackground(False)
        self.progressBar_4.setValue(100)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_5 = QProgressBar(self.groupBox_7)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setGeometry(QRect(340, 80, 51, 16))
        self.progressBar_5.setAutoFillBackground(False)
        self.progressBar_5.setValue(100)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_6 = QProgressBar(self.groupBox_7)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setGeometry(QRect(130, 100, 51, 16))
        self.progressBar_6.setAutoFillBackground(False)
        self.progressBar_6.setValue(100)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_7 = QProgressBar(self.groupBox_7)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setGeometry(QRect(340, 100, 51, 16))
        self.progressBar_7.setAutoFillBackground(False)
        self.progressBar_7.setValue(100)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_8 = QProgressBar(self.groupBox_7)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setGeometry(QRect(130, 120, 51, 16))
        self.progressBar_8.setAutoFillBackground(False)
        self.progressBar_8.setValue(100)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_9 = QProgressBar(self.groupBox_7)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setGeometry(QRect(340, 120, 51, 16))
        self.progressBar_9.setAutoFillBackground(False)
        self.progressBar_9.setValue(100)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_10 = QProgressBar(self.groupBox_7)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setGeometry(QRect(130, 140, 51, 16))
        self.progressBar_10.setAutoFillBackground(False)
        self.progressBar_10.setValue(100)
        self.progressBar_10.setTextVisible(False)
        self.progressBar_11 = QProgressBar(self.groupBox_7)
        self.progressBar_11.setObjectName(u"progressBar_11")
        self.progressBar_11.setGeometry(QRect(340, 140, 51, 16))
        self.progressBar_11.setAutoFillBackground(False)
        self.progressBar_11.setValue(100)
        self.progressBar_11.setTextVisible(False)
        self.progressBar_12 = QProgressBar(self.groupBox_7)
        self.progressBar_12.setObjectName(u"progressBar_12")
        self.progressBar_12.setGeometry(QRect(130, 160, 51, 16))
        self.progressBar_12.setAutoFillBackground(False)
        self.progressBar_12.setValue(100)
        self.progressBar_12.setTextVisible(False)
        self.progressBar_13 = QProgressBar(self.groupBox_7)
        self.progressBar_13.setObjectName(u"progressBar_13")
        self.progressBar_13.setGeometry(QRect(340, 160, 51, 16))
        self.progressBar_13.setAutoFillBackground(False)
        self.progressBar_13.setValue(100)
        self.progressBar_13.setTextVisible(False)
        self.progressBar_14 = QProgressBar(self.groupBox_7)
        self.progressBar_14.setObjectName(u"progressBar_14")
        self.progressBar_14.setGeometry(QRect(130, 180, 51, 16))
        self.progressBar_14.setAutoFillBackground(False)
        self.progressBar_14.setValue(100)
        self.progressBar_14.setTextVisible(False)
        self.progressBar_15 = QProgressBar(self.groupBox_7)
        self.progressBar_15.setObjectName(u"progressBar_15")
        self.progressBar_15.setGeometry(QRect(340, 180, 51, 16))
        self.progressBar_15.setAutoFillBackground(False)
        self.progressBar_15.setValue(100)
        self.progressBar_15.setTextVisible(False)
        self.progressBar_16 = QProgressBar(self.groupBox_7)
        self.progressBar_16.setObjectName(u"progressBar_16")
        self.progressBar_16.setGeometry(QRect(130, 200, 51, 16))
        self.progressBar_16.setAutoFillBackground(False)
        self.progressBar_16.setValue(100)
        self.progressBar_16.setTextVisible(False)
        self.progressBar_17 = QProgressBar(self.groupBox_7)
        self.progressBar_17.setObjectName(u"progressBar_17")
        self.progressBar_17.setGeometry(QRect(340, 200, 51, 16))
        self.progressBar_17.setAutoFillBackground(False)
        self.progressBar_17.setValue(100)
        self.progressBar_17.setTextVisible(False)
        self.progressBar_18 = QProgressBar(self.groupBox_7)
        self.progressBar_18.setObjectName(u"progressBar_18")
        self.progressBar_18.setGeometry(QRect(130, 220, 51, 16))
        self.progressBar_18.setAutoFillBackground(False)
        self.progressBar_18.setValue(100)
        self.progressBar_18.setTextVisible(False)
        self.progressBar_19 = QProgressBar(self.groupBox_7)
        self.progressBar_19.setObjectName(u"progressBar_19")
        self.progressBar_19.setGeometry(QRect(340, 220, 51, 16))
        self.progressBar_19.setAutoFillBackground(False)
        self.progressBar_19.setValue(100)
        self.progressBar_19.setTextVisible(False)
        self.progressBar_20 = QProgressBar(self.groupBox_7)
        self.progressBar_20.setObjectName(u"progressBar_20")
        self.progressBar_20.setGeometry(QRect(130, 240, 51, 16))
        self.progressBar_20.setAutoFillBackground(False)
        self.progressBar_20.setValue(100)
        self.progressBar_20.setTextVisible(False)
        self.progressBar_21 = QProgressBar(self.groupBox_7)
        self.progressBar_21.setObjectName(u"progressBar_21")
        self.progressBar_21.setGeometry(QRect(340, 240, 51, 16))
        self.progressBar_21.setAutoFillBackground(False)
        self.progressBar_21.setValue(100)
        self.progressBar_21.setTextVisible(False)
        self.progressBar_22 = QProgressBar(self.groupBox_7)
        self.progressBar_22.setObjectName(u"progressBar_22")
        self.progressBar_22.setGeometry(QRect(130, 260, 51, 16))
        self.progressBar_22.setAutoFillBackground(False)
        self.progressBar_22.setValue(100)
        self.progressBar_22.setTextVisible(False)
        self.progressBar_23 = QProgressBar(self.groupBox_7)
        self.progressBar_23.setObjectName(u"progressBar_23")
        self.progressBar_23.setGeometry(QRect(340, 260, 51, 16))
        self.progressBar_23.setAutoFillBackground(False)
        self.progressBar_23.setValue(100)
        self.progressBar_23.setTextVisible(False)
        self.progressBar_24 = QProgressBar(self.groupBox_7)
        self.progressBar_24.setObjectName(u"progressBar_24")
        self.progressBar_24.setGeometry(QRect(130, 280, 51, 16))
        self.progressBar_24.setAutoFillBackground(False)
        self.progressBar_24.setValue(100)
        self.progressBar_24.setTextVisible(False)
        self.progressBar_25 = QProgressBar(self.groupBox_7)
        self.progressBar_25.setObjectName(u"progressBar_25")
        self.progressBar_25.setGeometry(QRect(340, 280, 51, 16))
        self.progressBar_25.setAutoFillBackground(False)
        self.progressBar_25.setValue(100)
        self.progressBar_25.setTextVisible(False)
        self.progressBar_26 = QProgressBar(self.groupBox_7)
        self.progressBar_26.setObjectName(u"progressBar_26")
        self.progressBar_26.setGeometry(QRect(130, 300, 51, 16))
        self.progressBar_26.setAutoFillBackground(False)
        self.progressBar_26.setValue(100)
        self.progressBar_26.setTextVisible(False)
        self.progressBar_27 = QProgressBar(self.groupBox_7)
        self.progressBar_27.setObjectName(u"progressBar_27")
        self.progressBar_27.setGeometry(QRect(340, 300, 51, 16))
        self.progressBar_27.setAutoFillBackground(False)
        self.progressBar_27.setValue(100)
        self.progressBar_27.setTextVisible(False)
        self.progressBar_28 = QProgressBar(self.groupBox_7)
        self.progressBar_28.setObjectName(u"progressBar_28")
        self.progressBar_28.setGeometry(QRect(130, 320, 51, 16))
        self.progressBar_28.setAutoFillBackground(False)
        self.progressBar_28.setValue(100)
        self.progressBar_28.setTextVisible(False)
        self.progressBar_29 = QProgressBar(self.groupBox_7)
        self.progressBar_29.setObjectName(u"progressBar_29")
        self.progressBar_29.setGeometry(QRect(340, 320, 51, 16))
        self.progressBar_29.setAutoFillBackground(False)
        self.progressBar_29.setValue(100)
        self.progressBar_29.setTextVisible(False)
        self.progressBar_30 = QProgressBar(self.groupBox_7)
        self.progressBar_30.setObjectName(u"progressBar_30")
        self.progressBar_30.setGeometry(QRect(130, 340, 51, 16))
        self.progressBar_30.setAutoFillBackground(False)
        self.progressBar_30.setValue(100)
        self.progressBar_30.setTextVisible(False)
        self.progressBar_31 = QProgressBar(self.groupBox_7)
        self.progressBar_31.setObjectName(u"progressBar_31")
        self.progressBar_31.setGeometry(QRect(340, 340, 51, 16))
        self.progressBar_31.setAutoFillBackground(False)
        self.progressBar_31.setValue(100)
        self.progressBar_31.setTextVisible(False)
        self.progressBar_32 = QProgressBar(self.groupBox_7)
        self.progressBar_32.setObjectName(u"progressBar_32")
        self.progressBar_32.setGeometry(QRect(130, 360, 51, 16))
        self.progressBar_32.setAutoFillBackground(False)
        self.progressBar_32.setValue(100)
        self.progressBar_32.setTextVisible(False)
        self.progressBar_33 = QProgressBar(self.groupBox_7)
        self.progressBar_33.setObjectName(u"progressBar_33")
        self.progressBar_33.setGeometry(QRect(340, 360, 51, 16))
        self.progressBar_33.setAutoFillBackground(False)
        self.progressBar_33.setValue(100)
        self.progressBar_33.setTextVisible(False)
        self.progressBar_34 = QProgressBar(self.groupBox_7)
        self.progressBar_34.setObjectName(u"progressBar_34")
        self.progressBar_34.setGeometry(QRect(130, 380, 51, 16))
        self.progressBar_34.setAutoFillBackground(False)
        self.progressBar_34.setValue(100)
        self.progressBar_34.setTextVisible(False)
        self.progressBar_35 = QProgressBar(self.groupBox_7)
        self.progressBar_35.setObjectName(u"progressBar_35")
        self.progressBar_35.setGeometry(QRect(340, 380, 51, 16))
        self.progressBar_35.setAutoFillBackground(False)
        self.progressBar_35.setValue(100)
        self.progressBar_35.setTextVisible(False)
        self.progressBar_36 = QProgressBar(self.groupBox_7)
        self.progressBar_36.setObjectName(u"progressBar_36")
        self.progressBar_36.setGeometry(QRect(130, 400, 51, 16))
        self.progressBar_36.setAutoFillBackground(False)
        self.progressBar_36.setValue(100)
        self.progressBar_36.setTextVisible(False)
        self.progressBar_37 = QProgressBar(self.groupBox_7)
        self.progressBar_37.setObjectName(u"progressBar_37")
        self.progressBar_37.setGeometry(QRect(340, 400, 51, 16))
        self.progressBar_37.setAutoFillBackground(False)
        self.progressBar_37.setValue(100)
        self.progressBar_37.setTextVisible(False)
        self.progressBar_38 = QProgressBar(self.groupBox_7)
        self.progressBar_38.setObjectName(u"progressBar_38")
        self.progressBar_38.setGeometry(QRect(130, 420, 51, 16))
        self.progressBar_38.setAutoFillBackground(False)
        self.progressBar_38.setValue(100)
        self.progressBar_38.setTextVisible(False)
        self.progressBar_39 = QProgressBar(self.groupBox_7)
        self.progressBar_39.setObjectName(u"progressBar_39")
        self.progressBar_39.setGeometry(QRect(340, 420, 51, 16))
        self.progressBar_39.setAutoFillBackground(False)
        self.progressBar_39.setValue(100)
        self.progressBar_39.setTextVisible(False)
        self.progressBar_40 = QProgressBar(self.groupBox_7)
        self.progressBar_40.setObjectName(u"progressBar_40")
        self.progressBar_40.setGeometry(QRect(130, 440, 51, 16))
        self.progressBar_40.setAutoFillBackground(False)
        self.progressBar_40.setValue(100)
        self.progressBar_40.setTextVisible(False)
        self.progressBar_41 = QProgressBar(self.groupBox_7)
        self.progressBar_41.setObjectName(u"progressBar_41")
        self.progressBar_41.setGeometry(QRect(340, 440, 51, 16))
        self.progressBar_41.setAutoFillBackground(False)
        self.progressBar_41.setValue(100)
        self.progressBar_41.setTextVisible(False)
        self.progressBar_42 = QProgressBar(self.groupBox_7)
        self.progressBar_42.setObjectName(u"progressBar_42")
        self.progressBar_42.setGeometry(QRect(130, 460, 51, 16))
        self.progressBar_42.setAutoFillBackground(False)
        self.progressBar_42.setValue(100)
        self.progressBar_42.setTextVisible(False)
        self.progressBar_43 = QProgressBar(self.groupBox_7)
        self.progressBar_43.setObjectName(u"progressBar_43")
        self.progressBar_43.setGeometry(QRect(340, 460, 51, 16))
        self.progressBar_43.setAutoFillBackground(False)
        self.progressBar_43.setValue(100)
        self.progressBar_43.setTextVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton_Agregar.setText(QCoreApplication.translate("MainWindow", u"Guardar Valores", None))
        self.pushButton_Ejecutar.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        ___qtablewidgetitem = self.tablaPbloqueados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tablaPbloqueados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T. Bloqueo", None));
        self.label_titulo_ProceL_2.setText(QCoreApplication.translate("MainWindow", u"Procesos Bloqueados", None))
        self.textBox_Quantum.setText("")
        self.label_Numero_2.setText(QCoreApplication.translate("MainWindow", u"Quantum ", None))
        self.groupBox_2.setTitle("")
        self.groupBox_5.setTitle("")
        self.label_titulo_procesoEje.setText(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        self.label_operacion_4.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_tiempo_t.setText(QCoreApplication.translate("MainWindow", u"T. Transcurrido", None))
        self.label_tiempo_r.setText(QCoreApplication.translate("MainWindow", u"T. Restante", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_titulo_Nuevos_2.setText(QCoreApplication.translate("MainWindow", u"Proximo a ingresar", None))
        self.label_Numero_tamanio.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None))
        self.label_Numero_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_id_quantum.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
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
        self.label_titulo_quatum.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
        self.groupBox_6.setTitle("")
        self.label_titulo_ProcesoTableP.setText(QCoreApplication.translate("MainWindow", u"Tabla de paginas", None))
        self.groupBox_7.setTitle("")
        ___qtablewidgetitem8 = self.tablaPaginacionL.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N. Macro", None));
        ___qtablewidgetitem9 = self.tablaPaginacionL.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.tablaPaginacionL.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem11 = self.tablaPaginacionL.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem12 = self.tablaPaginacionL.verticalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem13 = self.tablaPaginacionL.verticalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem14 = self.tablaPaginacionL.verticalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem15 = self.tablaPaginacionL.verticalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem16 = self.tablaPaginacionL.verticalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem17 = self.tablaPaginacionL.verticalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem18 = self.tablaPaginacionL.verticalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem19 = self.tablaPaginacionL.verticalHeaderItem(10)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem20 = self.tablaPaginacionL.verticalHeaderItem(11)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem21 = self.tablaPaginacionL.verticalHeaderItem(12)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem22 = self.tablaPaginacionL.verticalHeaderItem(13)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem23 = self.tablaPaginacionL.verticalHeaderItem(14)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem24 = self.tablaPaginacionL.verticalHeaderItem(15)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem25 = self.tablaPaginacionL.verticalHeaderItem(16)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem26 = self.tablaPaginacionL.verticalHeaderItem(17)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem27 = self.tablaPaginacionL.verticalHeaderItem(18)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem28 = self.tablaPaginacionL.verticalHeaderItem(19)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem29 = self.tablaPaginacionL.verticalHeaderItem(20)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem30 = self.tablaPaginacionL.verticalHeaderItem(21)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"22", None));

        __sortingEnabled = self.tablaPaginacionL.isSortingEnabled()
        self.tablaPaginacionL.setSortingEnabled(False)
        ___qtablewidgetitem31 = self.tablaPaginacionL.item(0, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem32 = self.tablaPaginacionL.item(1, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem33 = self.tablaPaginacionL.item(2, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem34 = self.tablaPaginacionL.item(3, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem35 = self.tablaPaginacionL.item(4, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem36 = self.tablaPaginacionL.item(5, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem37 = self.tablaPaginacionL.item(6, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem38 = self.tablaPaginacionL.item(7, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem39 = self.tablaPaginacionL.item(8, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem40 = self.tablaPaginacionL.item(9, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem41 = self.tablaPaginacionL.item(10, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem42 = self.tablaPaginacionL.item(11, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem43 = self.tablaPaginacionL.item(12, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem44 = self.tablaPaginacionL.item(13, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem45 = self.tablaPaginacionL.item(14, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"28", None));
        ___qtablewidgetitem46 = self.tablaPaginacionL.item(15, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem47 = self.tablaPaginacionL.item(16, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"32", None));
        ___qtablewidgetitem48 = self.tablaPaginacionL.item(17, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem49 = self.tablaPaginacionL.item(18, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"36", None));
        ___qtablewidgetitem50 = self.tablaPaginacionL.item(19, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"38", None));
        ___qtablewidgetitem51 = self.tablaPaginacionL.item(20, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem52 = self.tablaPaginacionL.item(21, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"42", None));
        self.tablaPaginacionL.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem53 = self.tablaPaginacionR.horizontalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"N. Marco", None));
        ___qtablewidgetitem54 = self.tablaPaginacionR.verticalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem55 = self.tablaPaginacionR.verticalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem56 = self.tablaPaginacionR.verticalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem57 = self.tablaPaginacionR.verticalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem58 = self.tablaPaginacionR.verticalHeaderItem(4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem59 = self.tablaPaginacionR.verticalHeaderItem(5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem60 = self.tablaPaginacionR.verticalHeaderItem(6)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem61 = self.tablaPaginacionR.verticalHeaderItem(7)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem62 = self.tablaPaginacionR.verticalHeaderItem(8)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem63 = self.tablaPaginacionR.verticalHeaderItem(9)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem64 = self.tablaPaginacionR.verticalHeaderItem(10)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem65 = self.tablaPaginacionR.verticalHeaderItem(11)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem66 = self.tablaPaginacionR.verticalHeaderItem(12)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem67 = self.tablaPaginacionR.verticalHeaderItem(13)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem68 = self.tablaPaginacionR.verticalHeaderItem(14)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem69 = self.tablaPaginacionR.verticalHeaderItem(15)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem70 = self.tablaPaginacionR.verticalHeaderItem(16)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem71 = self.tablaPaginacionR.verticalHeaderItem(17)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem72 = self.tablaPaginacionR.verticalHeaderItem(18)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem73 = self.tablaPaginacionR.verticalHeaderItem(19)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem74 = self.tablaPaginacionR.verticalHeaderItem(20)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem75 = self.tablaPaginacionR.verticalHeaderItem(21)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"22", None));

        __sortingEnabled1 = self.tablaPaginacionR.isSortingEnabled()
        self.tablaPaginacionR.setSortingEnabled(False)
        ___qtablewidgetitem76 = self.tablaPaginacionR.item(0, 1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem77 = self.tablaPaginacionR.item(1, 1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem78 = self.tablaPaginacionR.item(2, 1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem79 = self.tablaPaginacionR.item(3, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem80 = self.tablaPaginacionR.item(4, 1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem81 = self.tablaPaginacionR.item(5, 1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem82 = self.tablaPaginacionR.item(6, 1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem83 = self.tablaPaginacionR.item(7, 1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem84 = self.tablaPaginacionR.item(8, 1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem85 = self.tablaPaginacionR.item(9, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem86 = self.tablaPaginacionR.item(10, 1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem87 = self.tablaPaginacionR.item(11, 1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem88 = self.tablaPaginacionR.item(12, 1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem89 = self.tablaPaginacionR.item(13, 1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"27", None));
        ___qtablewidgetitem90 = self.tablaPaginacionR.item(14, 1)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"29", None));
        ___qtablewidgetitem91 = self.tablaPaginacionR.item(15, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"31", None));
        ___qtablewidgetitem92 = self.tablaPaginacionR.item(16, 1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"33", None));
        ___qtablewidgetitem93 = self.tablaPaginacionR.item(17, 1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"35", None));
        ___qtablewidgetitem94 = self.tablaPaginacionR.item(18, 1)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"37", None));
        ___qtablewidgetitem95 = self.tablaPaginacionR.item(19, 1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"39", None));
        ___qtablewidgetitem96 = self.tablaPaginacionR.item(20, 1)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"41", None));
        ___qtablewidgetitem97 = self.tablaPaginacionR.item(21, 1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"43", None));
        self.tablaPaginacionR.setSortingEnabled(__sortingEnabled1)

    # retranslateUi


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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

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
        self.textBox_NumProcess.setGeometry(QRect(0, 160, 230, 35))
        self.textBox_NumProcess.setMinimumSize(QSize(60, 35))
        self.textBox_NumProcess.setMaximumSize(QSize(230, 35))
        self.textBox_NumProcess.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Numero = QLabel(self.groupBox_4)
        self.label_Numero.setObjectName(u"label_Numero")
        self.label_Numero.setGeometry(QRect(30, 120, 171, 31))
        self.label_Numero.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"")
        self.pushButton_Agregar = QPushButton(self.groupBox_4)
        self.pushButton_Agregar.setObjectName(u"pushButton_Agregar")
        self.pushButton_Agregar.setGeometry(QRect(0, 210, 111, 41))
        self.pushButton_Agregar.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"color: #FFFFFF;\n"
"font: 75 12pt \"Microsoft YaHei\";\n"
"border-radius: 10px;")
        self.pushButton_Ejecutar = QPushButton(self.groupBox_4)
        self.pushButton_Ejecutar.setObjectName(u"pushButton_Ejecutar")
        self.pushButton_Ejecutar.setGeometry(QRect(130, 210, 111, 41))
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

        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QRect(290, 10, 360, 689))
        self.groupBox_2.setSizeIncrement(QSize(6, 6))
        self.groupBox_2.setBaseSize(QSize(9, 6))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 300, 321, 311))
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
        self.textBox_Id_proceso.setGeometry(QRect(140, 260, 141, 35))
        self.textBox_Id_proceso.setMinimumSize(QSize(60, 35))
        self.textBox_Id_proceso.setMaximumSize(QSize(230, 35))
        self.textBox_Id_proceso.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_id = QLabel(self.groupBox_5)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setGeometry(QRect(10, 260, 31, 31))
        self.label_id.setStyleSheet(u"color:rgb(255, 255, 255);\n"
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
        if (self.tablaProcesos.columnCount() < 3):
            self.tablaProcesos.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        if (self.tablaProcesos.rowCount() < 2):
            self.tablaProcesos.setRowCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaProcesos.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaProcesos.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaProcesos.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaProcesos.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaProcesos.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaProcesos.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaProcesos.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaProcesos.setItem(1, 2, __qtablewidgetitem12)
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
        self.tablaProcesos.setRowCount(2)
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
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        self.tablaPTerminados.setObjectName(u"tablaPTerminados")
        self.tablaPTerminados.setEnabled(False)
        self.tablaPTerminados.setGeometry(QRect(120, 100, 311, 191))
        self.tablaPTerminados.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablaPTerminados.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPTerminados.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaPTerminados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaPTerminados.horizontalHeader().setDefaultSectionSize(104)
        self.tablaPTerminados.verticalHeader().setVisible(False)
        self.label_titulo_Cont = QLabel(self.groupBox_3)
        self.label_titulo_Cont.setObjectName(u"label_titulo_Cont")
        self.label_titulo_Cont.setGeometry(QRect(20, 630, 101, 31))
        self.label_titulo_Cont.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.textBox_contadorGlobal = QLineEdit(self.groupBox_3)
        self.textBox_contadorGlobal.setObjectName(u"textBox_contadorGlobal")
        self.textBox_contadorGlobal.setGeometry(QRect(140, 630, 71, 35))
        self.textBox_contadorGlobal.setMinimumSize(QSize(60, 35))
        self.textBox_contadorGlobal.setMaximumSize(QSize(230, 35))
        self.textBox_contadorGlobal.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_titulo_TiempoC = QLabel(self.groupBox_3)
        self.label_titulo_TiempoC.setObjectName(u"label_titulo_TiempoC")
        self.label_titulo_TiempoC.setGeometry(QRect(180, 310, 221, 31))
        self.label_titulo_TiempoC.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"\n"
"font: 63 13pt \"Segoe UI Semibold\";\n"
"")
        self.tablePTimeStats = QTableWidget(self.groupBox_3)
        if (self.tablePTimeStats.columnCount() < 7):
            self.tablePTimeStats.setColumnCount(7)
        font = QFont()
        font.setPointSize(8)
        font.setKerning(False)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setText(u"ID");
        __qtablewidgetitem16.setFont(font);
        self.tablePTimeStats.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        font1 = QFont()
        font1.setPointSize(8)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.tablePTimeStats.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setText(u"T.F");
        __qtablewidgetitem18.setFont(font1);
        self.tablePTimeStats.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.tablePTimeStats.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.tablePTimeStats.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.tablePTimeStats.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablePTimeStats.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.tablePTimeStats.setObjectName(u"tablePTimeStats")
        self.tablePTimeStats.setEnabled(False)
        self.tablePTimeStats.setGeometry(QRect(30, 350, 471, 271))
        self.tablePTimeStats.setAcceptDrops(True)
        self.tablePTimeStats.setAutoFillBackground(True)
        self.tablePTimeStats.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.tablePTimeStats.setFrameShadow(QFrame.Raised)
        self.tablePTimeStats.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablePTimeStats.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablePTimeStats.setAutoScroll(True)
        self.tablePTimeStats.setAutoScrollMargin(8)
        self.tablePTimeStats.setTabKeyNavigation(False)
        self.tablePTimeStats.setProperty("showDropIndicator", False)
        self.tablePTimeStats.setDragEnabled(True)
        self.tablePTimeStats.setDragDropMode(QAbstractItemView.DragOnly)
        self.tablePTimeStats.setAlternatingRowColors(False)
        self.tablePTimeStats.setShowGrid(True)
        self.tablePTimeStats.setWordWrap(True)
        self.tablePTimeStats.horizontalHeader().setVisible(True)
        self.tablePTimeStats.horizontalHeader().setCascadingSectionResizes(True)
        self.tablePTimeStats.horizontalHeader().setMinimumSectionSize(25)
        self.tablePTimeStats.horizontalHeader().setDefaultSectionSize(67)
        self.tablePTimeStats.horizontalHeader().setHighlightSections(True)
        self.tablePTimeStats.horizontalHeader().setProperty("showSortIndicator", True)
        self.tablePTimeStats.horizontalHeader().setStretchLastSection(True)
        self.tablePTimeStats.verticalHeader().setVisible(False)
        self.tablePTimeStats.verticalHeader().setCascadingSectionResizes(False)
        self.tablePTimeStats.verticalHeader().setHighlightSections(False)
        self.tablePTimeStats.verticalHeader().setProperty("showSortIndicator", False)
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
        self.groupBox_2.setTitle("")
        self.groupBox_5.setTitle("")
        self.label_titulo_procesoEje.setText(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        self.label_operacion_4.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_tiempo_t.setText(QCoreApplication.translate("MainWindow", u"T. Transcurrido", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_tiempo_r.setText(QCoreApplication.translate("MainWindow", u"T. Restante", None))
        ___qtablewidgetitem2 = self.tablaProcesos.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.tablaProcesos.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T. M\u00e1x", None));
        ___qtablewidgetitem4 = self.tablaProcesos.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T. Transcurrido", None));
        ___qtablewidgetitem5 = self.tablaProcesos.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nueva fila", None));
        ___qtablewidgetitem6 = self.tablaProcesos.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tablaProcesos.isSortingEnabled()
        self.tablaProcesos.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tablaProcesos.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tablaProcesos.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.tablaProcesos.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.tablaProcesos.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem11 = self.tablaProcesos.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.tablaProcesos.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.tablaProcesos.setSortingEnabled(__sortingEnabled)

        self.label_titulo_ProceL.setText(QCoreApplication.translate("MainWindow", u"Procesos listos", None))
        self.label_titulo_Nuevos.setText(QCoreApplication.translate("MainWindow", u"Nuevos:", None))
        self.groupBox_3.setTitle("")
        self.label_titulo_ProcesoT.setText(QCoreApplication.translate("MainWindow", u"Procesos Terminados", None))
        ___qtablewidgetitem13 = self.tablaPTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem14 = self.tablaPTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem15 = self.tablaPTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.label_titulo_Cont.setText(QCoreApplication.translate("MainWindow", u"Contador", None))
        self.textBox_contadorGlobal.setText("")
        self.label_titulo_TiempoC.setText(QCoreApplication.translate("MainWindow", u"Tiempos calculados", None))
        ___qtablewidgetitem16 = self.tablePTimeStats.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"T.L", None));
        ___qtablewidgetitem17 = self.tablePTimeStats.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"T.Ret", None));
        ___qtablewidgetitem18 = self.tablePTimeStats.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"T.Res", None));
        ___qtablewidgetitem19 = self.tablePTimeStats.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"T. E.", None));
        ___qtablewidgetitem20 = self.tablePTimeStats.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"T.S", None));
    # retranslateUi


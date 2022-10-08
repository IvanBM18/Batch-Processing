# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tableBCP.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGroupBox,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(789, 533)
        Form.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 761, 511))
        self.tableBCP = QTableWidget(self.groupBox)
        if (self.tableBCP.columnCount() < 12):
            self.tableBCP.setColumnCount(12)
        font = QFont()
        font.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        self.tableBCP.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableBCP.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableBCP.setObjectName(u"tableBCP")
        self.tableBCP.setEnabled(False)
        self.tableBCP.setGeometry(QRect(0, 0, 761, 511))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableBCP.sizePolicy().hasHeightForWidth())
        self.tableBCP.setSizePolicy(sizePolicy)
        self.tableBCP.setMinimumSize(QSize(761, 0))
        self.tableBCP.setMaximumSize(QSize(811, 16777215))
        self.tableBCP.setSizeIncrement(QSize(20, 0))
        palette = QPalette()
        brush = QBrush(QColor(44, 47, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.tableBCP.setPalette(palette)
        self.tableBCP.setLayoutDirection(Qt.LeftToRight)
        self.tableBCP.setAutoFillBackground(True)
        self.tableBCP.setStyleSheet(u"background-color: rgb(44, 47, 51);")
        self.tableBCP.setInputMethodHints(Qt.ImhNone)
        self.tableBCP.setFrameShape(QFrame.Box)
        self.tableBCP.setFrameShadow(QFrame.Sunken)
        self.tableBCP.setLineWidth(2)
        self.tableBCP.setMidLineWidth(2)
        self.tableBCP.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableBCP.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableBCP.setDragEnabled(True)
        self.tableBCP.setDragDropOverwriteMode(False)
        self.tableBCP.setAlternatingRowColors(False)
        self.tableBCP.setIconSize(QSize(0, 0))
        self.tableBCP.setShowGrid(True)
        self.tableBCP.setGridStyle(Qt.SolidLine)
        self.tableBCP.setSortingEnabled(False)
        self.tableBCP.setWordWrap(True)
        self.tableBCP.setCornerButtonEnabled(False)
        self.tableBCP.horizontalHeader().setVisible(True)
        self.tableBCP.horizontalHeader().setCascadingSectionResizes(False)
        self.tableBCP.horizontalHeader().setMinimumSectionSize(9)
        self.tableBCP.horizontalHeader().setDefaultSectionSize(62)
        self.tableBCP.horizontalHeader().setHighlightSections(False)
        self.tableBCP.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableBCP.horizontalHeader().setStretchLastSection(False)
        self.tableBCP.verticalHeader().setVisible(False)
        self.tableBCP.verticalHeader().setCascadingSectionResizes(False)
        self.tableBCP.verticalHeader().setMinimumSectionSize(6)
        self.tableBCP.verticalHeader().setDefaultSectionSize(25)
        self.tableBCP.verticalHeader().setHighlightSections(False)
        self.tableBCP.verticalHeader().setProperty("showSortIndicator", False)
        self.tableBCP.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableBCP.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableBCP.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Operacion", None));
        ___qtablewidgetitem2 = self.tableBCP.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Resultado", None));
        ___qtablewidgetitem3 = self.tableBCP.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Estado", None));
        ___qtablewidgetitem4 = self.tableBCP.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"T. Max", None));
        ___qtablewidgetitem5 = self.tableBCP.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"T. Llegada", None));
        ___qtablewidgetitem6 = self.tableBCP.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"T. Espera", None));
        ___qtablewidgetitem7 = self.tableBCP.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"T. Fin", None));
        ___qtablewidgetitem8 = self.tableBCP.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"T. Res", None));
        ___qtablewidgetitem9 = self.tableBCP.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"T. Ret", None));
        ___qtablewidgetitem10 = self.tableBCP.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"T. Serv", None));
        ___qtablewidgetitem11 = self.tableBCP.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"T. Bloq", None));
    # retranslateUi


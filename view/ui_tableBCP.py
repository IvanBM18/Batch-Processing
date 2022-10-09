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
        Form.resize(779, 526)
        Form.setStyleSheet(u"background-color: rgb(52, 62, 64);")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 761, 511))
        self.tableTStats = QTableWidget(self.groupBox)
        if (self.tableTStats.columnCount() < 11):
            self.tableTStats.setColumnCount(11)
        font = QFont()
        font.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        self.tableTStats.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableTStats.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableTStats.setObjectName(u"tableTStats")
        self.tableTStats.setEnabled(False)
        self.tableTStats.setGeometry(QRect(0, 0, 761, 511))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableTStats.sizePolicy().hasHeightForWidth())
        self.tableTStats.setSizePolicy(sizePolicy)
        self.tableTStats.setMinimumSize(QSize(761, 511))
        self.tableTStats.setMaximumSize(QSize(811, 511))
        self.tableTStats.setSizeIncrement(QSize(20, 0))
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
        self.tableTStats.setPalette(palette)
        self.tableTStats.setLayoutDirection(Qt.LeftToRight)
        self.tableTStats.setAutoFillBackground(True)
        self.tableTStats.setStyleSheet(u"background-color: rgb(44, 47, 51);")
        self.tableTStats.setInputMethodHints(Qt.ImhNone)
        self.tableTStats.setFrameShape(QFrame.Box)
        self.tableTStats.setFrameShadow(QFrame.Sunken)
        self.tableTStats.setLineWidth(2)
        self.tableTStats.setMidLineWidth(2)
        self.tableTStats.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableTStats.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableTStats.setDragEnabled(True)
        self.tableTStats.setDragDropOverwriteMode(False)
        self.tableTStats.setAlternatingRowColors(False)
        self.tableTStats.setIconSize(QSize(0, 0))
        self.tableTStats.setShowGrid(True)
        self.tableTStats.setGridStyle(Qt.SolidLine)
        self.tableTStats.setSortingEnabled(False)
        self.tableTStats.setWordWrap(True)
        self.tableTStats.setCornerButtonEnabled(False)
        self.tableTStats.horizontalHeader().setVisible(True)
        self.tableTStats.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTStats.horizontalHeader().setMinimumSectionSize(9)
        self.tableTStats.horizontalHeader().setDefaultSectionSize(62)
        self.tableTStats.horizontalHeader().setHighlightSections(False)
        self.tableTStats.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableTStats.horizontalHeader().setStretchLastSection(False)
        self.tableTStats.verticalHeader().setVisible(False)
        self.tableTStats.verticalHeader().setCascadingSectionResizes(False)
        self.tableTStats.verticalHeader().setMinimumSectionSize(6)
        self.tableTStats.verticalHeader().setDefaultSectionSize(25)
        self.tableTStats.verticalHeader().setHighlightSections(False)
        self.tableTStats.verticalHeader().setProperty("showSortIndicator", False)
        self.tableTStats.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableTStats.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableTStats.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Operacion", None));
        ___qtablewidgetitem2 = self.tableTStats.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Resultado", None));
        ___qtablewidgetitem3 = self.tableTStats.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Estado", None));
        ___qtablewidgetitem4 = self.tableTStats.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"T. LL", None));
        ___qtablewidgetitem5 = self.tableTStats.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"T. Fin", None));
        ___qtablewidgetitem6 = self.tableTStats.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"T. Ret", None));
        ___qtablewidgetitem7 = self.tableTStats.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"T. Esp", None));
        ___qtablewidgetitem8 = self.tableTStats.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"T.Serv", None));
        ___qtablewidgetitem9 = self.tableTStats.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"T. Rest", None));
        ___qtablewidgetitem10 = self.tableTStats.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"T.Resp", None));
    # retranslateUi


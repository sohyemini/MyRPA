# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(284, 277)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 41, 9))
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(70, 40, 161, 91))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 170, 61, 16))
        self.leName = QLineEdit(Dialog)
        self.leName.setObjectName(u"leName")
        self.leName.setGeometry(QRect(110, 170, 113, 20))
        self.pbConfirm = QPushButton(Dialog)
        self.pbConfirm.setObjectName(u"pbConfirm")
        self.pbConfirm.setGeometry(QRect(80, 230, 56, 17))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 230, 56, 17))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\ucc57GPT", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Your Name", None))
        self.pbConfirm.setText(QCoreApplication.translate("Dialog", u"\ud655\uc778", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi


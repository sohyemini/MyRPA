# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'excelComp.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(553, 214)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.leOri = QLineEdit(Dialog)
        self.leOri.setObjectName(u"leOri")
        self.leOri.setEnabled(False)
        self.leOri.setGeometry(QRect(120, 20, 411, 20))
        self.pbOri = QPushButton(Dialog)
        self.pbOri.setObjectName(u"pbOri")
        self.pbOri.setGeometry(QRect(30, 20, 81, 21))
        font = QFont()
        font.setPointSize(11)
        self.pbOri.setFont(font)
        self.pbComp = QPushButton(Dialog)
        self.pbComp.setObjectName(u"pbComp")
        self.pbComp.setGeometry(QRect(30, 60, 81, 21))
        self.pbComp.setFont(font)
        self.pbOut = QPushButton(Dialog)
        self.pbOut.setObjectName(u"pbOut")
        self.pbOut.setGeometry(QRect(30, 100, 81, 21))
        self.pbOut.setFont(font)
        self.leComp = QLineEdit(Dialog)
        self.leComp.setObjectName(u"leComp")
        self.leComp.setEnabled(False)
        self.leComp.setGeometry(QRect(120, 60, 411, 20))
        self.leOut = QLineEdit(Dialog)
        self.leOut.setObjectName(u"leOut")
        self.leOut.setEnabled(False)
        self.leOut.setGeometry(QRect(120, 100, 411, 20))
        self.pbExec = QPushButton(Dialog)
        self.pbExec.setObjectName(u"pbExec")
        self.pbExec.setGeometry(QRect(330, 160, 91, 41))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.pbExec.setFont(font1)
        self.pbQuit = QPushButton(Dialog)
        self.pbQuit.setObjectName(u"pbQuit")
        self.pbQuit.setGeometry(QRect(442, 160, 91, 41))
        self.pbQuit.setFont(font1)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 140, 221, 61))
        self.groupBox.setFont(font)
        self.rbStatic = QRadioButton(self.groupBox)
        self.rbStatic.setObjectName(u"rbStatic")
        self.rbStatic.setGeometry(QRect(10, 30, 91, 16))
        self.rbStatic.setFont(font)
        self.rbKey = QRadioButton(self.groupBox)
        self.rbKey.setObjectName(u"rbKey")
        self.rbKey.setGeometry(QRect(110, 30, 91, 16))
        self.rbKey.setFont(font)
        self.groupBox.raise_()
        self.leOri.raise_()
        self.pbOri.raise_()
        self.pbComp.raise_()
        self.pbOut.raise_()
        self.leComp.raise_()
        self.leOut.raise_()
        self.pbExec.raise_()
        self.pbQuit.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"RPA \uc5d1\uc140\ube44\uad50", None))
        self.pbOri.setText(QCoreApplication.translate("Dialog", u"\uc6d0\ubcf8\ud30c\uc77c", None))
        self.pbComp.setText(QCoreApplication.translate("Dialog", u"\ube44\uad50\ud30c\uc77c", None))
        self.pbOut.setText(QCoreApplication.translate("Dialog", u"\ucd9c\ub825\ud30c\uc77c", None))
        self.pbExec.setText(QCoreApplication.translate("Dialog", u"\ube44\uad50\uc2e4\ud589", None))
        self.pbQuit.setText(QCoreApplication.translate("Dialog", u"\uc885 \ub8cc", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Type", None))
        self.rbStatic.setText(QCoreApplication.translate("Dialog", u"\uace0\uc815\ud3ec\ub9f7", None))
        self.rbKey.setText(QCoreApplication.translate("Dialog", u"\uad6c\ubd84\ucf54\ub4dc", None))
    # retranslateUi


# -*- coding: utf-8 -*-
from PyQt6.QtGui import QIcon
from PySide6 import QtGui
################################################################################
## Form generated from reading UI file 'untitled3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, Signal)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPlainTextEdit, QPushButton, QScrollArea,
                               QSizePolicy, QVBoxLayout, QWidget)

from PlainTextEdit_Rewite import MyPlainTextEdit


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 662)
        MainWindow.setStyleSheet(u"")
        MainWindow.setWindowTitle("Jine")
        MainWindow.setWindowIcon(QtGui.QIcon('./file/background/1.ico'))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\n"
                                      "background-color: rgb(238, 152, 238);\n"
                                      "}\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 386, 483))
        self.scrollAreaWidgetContents.setStyleSheet(
            u"QWidget#scrollAreaWidgetContents{\\nborder-image: url(:/\u80cc\u666f/JINEBG.png);\\n}")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 5, -1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout_6.addWidget(self.frame)

        self.mywidget = QWidget(self.centralwidget)
        self.mywidget.setObjectName(u"mywidget")
        self.mywidget.setStyleSheet(u"QWidget#mywidget{\n"
                                    "	background-color: rgb(213, 183, 222);}\n"
                                    "")
        self.verticalLayout_3 = QVBoxLayout(self.mywidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 1, 16, 1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_love = ClickableLabel(self.mywidget)
        self.label_love.setObjectName(u"label_love")
        self.label_love.setPixmap(QPixmap(u"file/emoji/love.png"))

        self.horizontalLayout_3.addWidget(self.label_love, 0, Qt.AlignHCenter)

        self.label_idc = ClickableLabel(self.mywidget)
        self.label_idc.setObjectName(u"label_idc")
        self.label_idc.setPixmap(QPixmap(u"file/emoji/idc.png"))

        self.horizontalLayout_3.addWidget(self.label_idc, 0, Qt.AlignHCenter)

        self.label_ok = ClickableLabel(self.mywidget)
        self.label_ok.setObjectName(u"label_ok")
        self.label_ok.setPixmap(QPixmap(u"file/emoji/ok.png"))

        self.horizontalLayout_3.addWidget(self.label_ok, 0, Qt.AlignHCenter)

        self.label_die = ClickableLabel(self.mywidget)
        self.label_die.setObjectName(u"label_die")
        self.label_die.setTextFormat(Qt.AutoText)
        self.label_die.setPixmap(QPixmap(u"file/emoji/die.png"))
        self.label_die.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_die, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_omg = ClickableLabel(self.mywidget)
        self.label_omg.setObjectName(u"label_omg")
        self.label_omg.setPixmap(QPixmap(u"file/emoji/omg.png"))

        self.horizontalLayout_4.addWidget(self.label_omg, 0, Qt.AlignHCenter)

        self.label_sorry = ClickableLabel(self.mywidget)
        self.label_sorry.setObjectName(u"label_sorry")
        self.label_sorry.setPixmap(QPixmap(u"file/emoji/sorry.png"))

        self.horizontalLayout_4.addWidget(self.label_sorry, 0, Qt.AlignHCenter)

        self.label_cry = ClickableLabel(self.mywidget)
        self.label_cry.setObjectName(u"label_cry")
        self.label_cry.setPixmap(QPixmap(u"file/emoji/cry.png"))

        self.horizontalLayout_4.addWidget(self.label_cry, 0, Qt.AlignHCenter)

        self.label_this = ClickableLabel(self.mywidget)
        self.label_this.setObjectName(u"label_this")
        self.label_this.setPixmap(QPixmap(u"file/emoji/this.png"))

        self.horizontalLayout_4.addWidget(self.label_this, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 6)
        self.plainTextEdit = MyPlainTextEdit(self.mywidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Zpix"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(Qt.LeftToRight)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
                                         "	border-radius:15px;\n"
                                         "\n"
                                         "	background-color: #edceeb;\n"
                                         "	font: 12pt \"Zpix\";\n"
                                         "}")
        self.plainTextEdit.setCenterOnScroll(False)

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.pushButton = QPushButton(self.mywidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setSizeIncrement(QSize(0, 0))
        self.pushButton.setBaseSize(QSize(1, 0))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_6.addWidget(self.mywidget)

        self.verticalLayout_6.setStretch(0, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("JINE", u"JINE", None))
        self.label_love.setText("")
        self.label_idc.setText("")
        self.label_ok.setText("")
        self.label_die.setText("")
        self.label_omg.setText("")
        self.label_sorry.setText("")
        self.label_cry.setText("")
        self.label_this.setText("")
        # if QT_CONFIG(statustip)
        self.plainTextEdit.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
    # retranslateUi

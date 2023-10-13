# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled4.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPlainTextEdit, QPushButton, QScrollArea,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(349, 556)
        MainWindow.setStyleSheet(u"")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 345, 377))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents{\\nborder-image: url(:/\u80cc\u666f/JINEBG.png);\\n}")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 5, -1)
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 200))
        self.widget.setMaximumSize(QSize(200, 200))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(45, 45))
        self.label.setPixmap(QPixmap(u"../file/background/1.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/\u80cc\u666f/1.jpg"))

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.frame)

        self.mywidget = QWidget(self.centralwidget)
        self.mywidget.setObjectName(u"mywidget")
        self.mywidget.setStyleSheet(u"QWidget#mywidget{\n"
"border-image: url(:/\u80cc\u666f/emoji_bgfull.png);}")
        self.verticalLayout_3 = QVBoxLayout(self.mywidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 1, 16, 1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.mywidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/love.png"))

        self.horizontalLayout_3.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.mywidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/idc.png"))

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.mywidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/ok.png"))

        self.horizontalLayout_3.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.mywidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setTextFormat(Qt.AutoText)
        self.label_11.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/ded.png"))
        self.label_11.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_11, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.mywidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/omg.png"))

        self.horizontalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.mywidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/sorry.png"))

        self.horizontalLayout_4.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.mywidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/sad.png"))

        self.horizontalLayout_4.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.mywidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"../../downLoad/Needy-Streamer-Overload-master/@Resources/Images/JINE/this.png"))

        self.horizontalLayout_4.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 6)
        self.plainTextEdit = QPlainTextEdit(self.mywidget)
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

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_6.addWidget(self.mywidget)

        self.verticalLayout_6.setStretch(0, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_9.setText("")
        self.label_3.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_4.setText("")
        self.label_13.setText("")
        self.label_12.setText("")
        self.label_14.setText("")
#if QT_CONFIG(statustip)
        self.plainTextEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


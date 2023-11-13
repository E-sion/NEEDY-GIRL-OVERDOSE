# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

from qfluentwidgets import (LineEdit, PixmapLabel, PushButton)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(419, 704)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 390, 301, 71))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_omg = QLabel(self.layoutWidget)
        self.label_omg.setObjectName(u"label_omg")
        self.label_omg.setPixmap(QPixmap(u"../file/emoji/omg.png"))

        self.horizontalLayout_4.addWidget(self.label_omg, 0, Qt.AlignHCenter)

        self.label_sorry = QLabel(self.layoutWidget)
        self.label_sorry.setObjectName(u"label_sorry")
        self.label_sorry.setPixmap(QPixmap(u":/files/emoji/sorry.png"))

        self.horizontalLayout_4.addWidget(self.label_sorry, 0, Qt.AlignHCenter)

        self.label_cry = QLabel(self.layoutWidget)
        self.label_cry.setObjectName(u"label_cry")
        self.label_cry.setPixmap(QPixmap(u":/files/emoji/cry.png"))

        self.horizontalLayout_4.addWidget(self.label_cry)

        self.label_this = QLabel(self.layoutWidget)
        self.label_this.setObjectName(u"label_this")
        self.label_this.setPixmap(QPixmap(u":/files/emoji/this.png"))

        self.horizontalLayout_4.addWidget(self.label_this, 0, Qt.AlignHCenter)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(50, 300, 301, 71))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_love_2 = QLabel(self.layoutWidget_2)
        self.label_love_2.setObjectName(u"label_love_2")
        self.label_love_2.setPixmap(QPixmap(u"../file/emoji/love.png"))

        self.horizontalLayout_5.addWidget(self.label_love_2)

        self.label_idc_2 = QLabel(self.layoutWidget_2)
        self.label_idc_2.setObjectName(u"label_idc_2")
        self.label_idc_2.setPixmap(QPixmap(u":/files/emoji/idc.png"))

        self.horizontalLayout_5.addWidget(self.label_idc_2)

        self.label_ok_2 = QLabel(self.layoutWidget_2)
        self.label_ok_2.setObjectName(u"label_ok_2")
        self.label_ok_2.setPixmap(QPixmap(u":/files/emoji/ok.png"))

        self.horizontalLayout_5.addWidget(self.label_ok_2, 0, Qt.AlignHCenter)

        self.label_die_2 = QLabel(self.layoutWidget_2)
        self.label_die_2.setObjectName(u"label_die_2")
        self.label_die_2.setTextFormat(Qt.AutoText)
        self.label_die_2.setPixmap(QPixmap(u":/files/emoji/die.png"))
        self.label_die_2.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_die_2, 0, Qt.AlignHCenter)

        self.PixmapLabel = PixmapLabel(self.centralwidget)
        self.PixmapLabel.setObjectName(u"PixmapLabel")
        self.PixmapLabel.setGeometry(QRect(150, 60, 81, 81))
        self.PixmapLabel.setPixmap(QPixmap(u"../file/emoji/love.png"))
        self.PushButton = PushButton(self.centralwidget)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(241, 531, 111, 41))
        self.LineEdit = LineEdit(self.centralwidget)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setGeometry(QRect(70, 520, 128, 33))
        self.LineEdit.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0,"
                        " 150);\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 620, 113, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 419, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_omg.setText("")
        self.label_sorry.setText("")
        self.label_cry.setText("")
        self.label_this.setText("")
        self.label_love_2.setText("")
        self.label_idc_2.setText("")
        self.label_ok_2.setText("")
        self.label_die_2.setText("")
        self.PushButton.setText(QCoreApplication.translate("MainWindow", u"Push button", None))
    # retranslateUi


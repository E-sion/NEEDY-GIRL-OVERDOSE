# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emoji_textline.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PushButton)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(368, 402)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_love_2 = QLabel(Form)
        self.label_love_2.setObjectName(u"label_love_2")
        self.label_love_2.setPixmap(QPixmap(u"../file/emoji/love.png"))

        self.horizontalLayout_5.addWidget(self.label_love_2, 0, Qt.AlignHCenter)

        self.label_idc_2 = QLabel(Form)
        self.label_idc_2.setObjectName(u"label_idc_2")
        self.label_idc_2.setPixmap(QPixmap(u":/files/emoji/idc.png"))

        self.horizontalLayout_5.addWidget(self.label_idc_2, 0, Qt.AlignHCenter)

        self.label_ok_2 = QLabel(Form)
        self.label_ok_2.setObjectName(u"label_ok_2")
        self.label_ok_2.setPixmap(QPixmap(u":/files/emoji/ok.png"))

        self.horizontalLayout_5.addWidget(self.label_ok_2, 0, Qt.AlignHCenter)

        self.label_die_2 = QLabel(Form)
        self.label_die_2.setObjectName(u"label_die_2")
        self.label_die_2.setTextFormat(Qt.AutoText)
        self.label_die_2.setPixmap(QPixmap(u":/files/emoji/die.png"))
        self.label_die_2.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_die_2, 0, Qt.AlignHCenter)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_omg = QLabel(Form)
        self.label_omg.setObjectName(u"label_omg")
        self.label_omg.setPixmap(QPixmap(u"../file/emoji/omg.png"))

        self.horizontalLayout_4.addWidget(self.label_omg, 0, Qt.AlignHCenter)

        self.label_sorry = QLabel(Form)
        self.label_sorry.setObjectName(u"label_sorry")
        self.label_sorry.setPixmap(QPixmap(u":/files/emoji/sorry.png"))

        self.horizontalLayout_4.addWidget(self.label_sorry, 0, Qt.AlignHCenter)

        self.label_this = QLabel(Form)
        self.label_this.setObjectName(u"label_this")
        self.label_this.setPixmap(QPixmap(u":/files/emoji/this.png"))

        self.horizontalLayout_4.addWidget(self.label_this, 0, Qt.AlignHCenter)

        self.label_cry = QLabel(Form)
        self.label_cry.setObjectName(u"label_cry")
        self.label_cry.setPixmap(QPixmap(u":/files/emoji/cry.png"))

        self.horizontalLayout_4.addWidget(self.label_cry, 0, Qt.AlignHCenter)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 8, -1)
        self.LineEdit = LineEdit(Form)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
                                    "\n"
                                    "    background-color:#f8e2fd;\n"
                                    "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                    "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                    "    border-radius: 15px;\n"
                                    "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                    "	font: 500 11pt \"Zpix\";\n"
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
                                    "    background-color: #f8e2fd;\n"
                                    "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                    "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                    "}\n"
                                    "\n"
                                    "TextEdit:focus,\n"
                                    "PlainTextEdit:focus {\n"
                                    "    border-bottom: 1px solid #009faa;\n"
                                    "    background-color: #f8e2fd;\n"
                                    "}\n"
                                    "\n"
                                    "LineEdit:disabled, TextEdit:disabled,\n"
                                    "PlainTextEdit:disabled {\n"
                                    "    color: rgba(0, 0, 0, 150);\n"
                                    "    background-color: rgba(249, 249, 249, 0.3);\n"
                                    "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                    "    border-bottom: 1px solid"
                                    " rgba(0, 0, 0, 13);\n"
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

        self.horizontalLayout.addWidget(self.LineEdit)

        self.PushButton = PushButton(Form)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
                                      "    color: black;\n"
                                      "    background: rgba(255, 255, 255, 0.7);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                      "    border-radius: 8px;\n"
                                      "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
                                      "    padding: 5px 12px 6px 12px;\n"
                                      "    outline: none;\n"
                                      "}\n"
                                      "\n"
                                      "ToolButton {\n"
                                      "    padding: 5px 9px 6px 8px;\n"
                                      "}\n"
                                      "\n"
                                      "PushButton[hasIcon=false] {\n"
                                      "    padding: 5px 12px 6px 12px;\n"
                                      "}\n"
                                      "\n"
                                      "PushButton[hasIcon=true] {\n"
                                      "    padding: 5px 12px 6px 36px;\n"
                                      "}\n"
                                      "\n"
                                      "DropDownToolButton, PrimaryDropDownToolButton {\n"
                                      "    padding: 5px 31px 6px 8px;\n"
                                      "}\n"
                                      "\n"
                                      "DropDownPushButton[hasIcon=false],\n"
                                      "PrimaryDropDownPushButton[hasIcon=false] {\n"
                                      "    padding: 5px 31px 6px 12px;\n"
                                      "}\n"
                                      "\n"
                                      "DropDownPushButton[hasIcon=true],\n"
                                      "PrimaryDropDownPushButton[hasIcon=true] {\n"
                                      "    padding: 5px 31px 6px 36px;\n"
                                      "}\n"
                                      "\n"
                                      "PushButton:hover, ToolButton:hover, ToggleButton:hover, To"
                                      "ggleToolButton:hover {\n"
                                      "    background: rgba(249, 249, 249, 0.5);\n"
                                      "}\n"
                                      "\n"
                                      "PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
                                      "    color: rgba(0, 0, 0, 0.63);\n"
                                      "    background: rgba(249, 249, 249, 0.3);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
                                      "}\n"
                                      "\n"
                                      "PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
                                      "    color: rgba(0, 0, 0, 0.36);\n"
                                      "    background: rgba(249, 249, 249, 0.3);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.06);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "PrimaryPushButton,\n"
                                      "PrimaryToolButton,\n"
                                      "ToggleButton:checked,\n"
                                      "ToggleToolButton:checked {\n"
                                      "    color: white;\n"
                                      "    background-color: #009faa;\n"
                                      "    border: 1px solid #00a7b3;\n"
                                      "    border-bottom: 1px solid #007780;\n"
                                      "}\n"
                                      "\n"
                                      "PrimaryPushButton:hover,\n"
                                      "PrimaryToolButton:hover,\n"
                                      "ToggleButton:checked:hover,\n"
                                      "ToggleToolButton:checked:hover {\n"
                                      "    background-color: #00a7b3"
                                      ";\n"
                                      "    border: 1px solid #2daab3;\n"
                                      "    border-bottom: 1px solid #007780;\n"
                                      "}\n"
                                      "\n"
                                      "PrimaryPushButton:pressed,\n"
                                      "PrimaryToolButton:pressed,\n"
                                      "ToggleButton:checked:pressed,\n"
                                      "ToggleToolButton:checked:pressed {\n"
                                      "    color: rgba(255, 255, 255, 0.63);\n"
                                      "    background-color: #3eabb3;\n"
                                      "    border: 1px solid #3eabb3;\n"
                                      "}\n"
                                      "\n"
                                      "PrimaryPushButton:disabled,\n"
                                      "PrimaryToolButton:disabled,\n"
                                      "ToggleButton:checked:disabled,\n"
                                      "ToggleToolButton:checked:disabled {\n"
                                      "    color: rgba(255, 255, 255, 0.9);\n"
                                      "    background-color: rgb(205, 205, 205);\n"
                                      "    border: 1px solid rgb(205, 205, 205);\n"
                                      "}\n"
                                      "\n"
                                      "SplitDropButton,\n"
                                      "PrimarySplitDropButton {\n"
                                      "    border-left: none;\n"
                                      "    border-top-left-radius: 0;\n"
                                      "    border-bottom-left-radius: 0;\n"
                                      "}\n"
                                      "\n"
                                      "#splitPushButton,\n"
                                      "#splitToolButton,\n"
                                      "#primarySplitPushButton,\n"
                                      "#primarySplitToolButton {\n"
                                      "    border-top-right-radius: 0;\n"
                                      "    border-bottom-right-radius: 0;\n"
                                      "}\n"
                                      "\n"
                                      "#splitPushButton:pressed,\n"
                                      "#splitTool"
                                      "Button:pressed,\n"
                                      "SplitDropButton:pressed {\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                      "}\n"
                                      "\n"
                                      "PrimarySplitDropButton:pressed {\n"
                                      "    border-bottom: 1px solid #007780;\n"
                                      "}\n"
                                      "\n"
                                      "#primarySplitPushButton, #primarySplitToolButton {\n"
                                      "    border-right: 1px solid #3eabb3;\n"
                                      "}\n"
                                      "\n"
                                      "#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
                                      "    border-bottom: 1px solid #007780;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton {\n"
                                      "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
                                      "    padding: 6px 12px 6px 12px;\n"
                                      "    color: #009faa;\n"
                                      "    border: none;\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton[hasIcon=false] {\n"
                                      "    padding: 6px 12px 6px 12px;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton[hasIcon=true] {\n"
                                      "    padding: 6px 12px 6px 36px;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton:hover {\n"
                                      "    color: #009faa;\n"
                                      "    background-color: rgba(0, 0, 0, 10);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton:pressed {\n"
                                      "    color: #009faa;\n"
                                      ""
                                      "    background-color: rgba(0, 0, 0, 6);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton:disabled {\n"
                                      "    color: rgba(0, 0, 0, 0.43);\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "RadioButton {\n"
                                      "    min-height: 24px;\n"
                                      "    max-height: 24px;\n"
                                      "    background-color: transparent;\n"
                                      "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator {\n"
                                      "    width: 18px;\n"
                                      "    height: 18px;\n"
                                      "    border-radius: 11px;\n"
                                      "    border: 2px solid #999999;\n"
                                      "    background-color: rgba(0, 0, 0, 5);\n"
                                      "    margin-right: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:hover {\n"
                                      "    background-color: rgba(0, 0, 0, 0);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:pressed {\n"
                                      "    border: 2px solid #bbbbbb;\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 rgb(225, 2"
                                      "24, 223),\n"
                                      "            stop:1 rgb(225, 224, 223));\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:checked {\n"
                                      "    height: 22px;\n"
                                      "    width: 22px;\n"
                                      "    border: none;\n"
                                      "    border-radius: 11px;\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 #009faa,\n"
                                      "            stop:1 #009faa);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:checked:hover {\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.6 rgb(255, 255, 255),\n"
                                      "            stop:0.7 #009faa,\n"
                                      "            stop:1 #009faa);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:checked:pressed {\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 #0"
                                      "09faa,\n"
                                      "            stop:1 #009faa);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton:disabled {\n"
                                      "    color: rgba(0, 0, 0, 110);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:disabled {\n"
                                      "    border: 2px solid #bbbbbb;\n"
                                      "    background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:disabled:checked {\n"
                                      "    border: none;\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
                                      "            stop:1 rgba(0, 0, 0, 0.2169));\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton,\n"
                                      "TransparentToggleToolButton,\n"
                                      "TransparentDropDownToolButton,\n"
                                      "TransparentPushButton,\n"
                                      "TransparentDropDownPushButton,\n"
                                      "TransparentTogglePushButton {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "    border-radius: 5px;\n"
                                      "    margin: 0;\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton:hover,\n"
                                      "TransparentToggleToolButton:hover,\n"
                                      "TransparentDropDownToolButton:ho"
                                      "ver,\n"
                                      "TransparentPushButton:hover,\n"
                                      "TransparentDropDownPushButton:hover,\n"
                                      "TransparentTogglePushButton:hover {\n"
                                      "    background-color: rgba(0, 0, 0, 9);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton:pressed,\n"
                                      "TransparentToggleToolButton:pressed,\n"
                                      "TransparentDropDownToolButton:pressed,\n"
                                      "TransparentPushButton:pressed,\n"
                                      "TransparentDropDownPushButton:pressed,\n"
                                      "TransparentTogglePushButton:pressed {\n"
                                      "    background-color: rgba(0, 0, 0, 6);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton:disabled,\n"
                                      "TransparentToggleToolButton:disabled,\n"
                                      "TransparentDropDownToolButton:disabled,\n"
                                      "TransprentPushButton:disabled,\n"
                                      "TransparentDropDownPushButton:disabled,\n"
                                      "TransprentTogglePushButton:disabled {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "PillPushButton,\n"
                                      "PillPushButton:hover,\n"
                                      "PillPushButton:pressed,\n"
                                      "PillPushButton:disabled,\n"
                                      "PillPushButton:checked,\n"
                                      "PillPushButton:checked:hover,\n"
                                      "PillPushButton:checked:p"
                                      "ressed,\n"
                                      "PillPushButton:disabled:checked,\n"
                                      "PillToolButton,\n"
                                      "PillToolButton:hover,\n"
                                      "PillToolButton:pressed,\n"
                                      "PillToolButton:disabled,\n"
                                      "PillToolButton:checked,\n"
                                      "PillToolButton:checked:hover,\n"
                                      "PillToolButton:checked:pressed,\n"
                                      "PillToolButton:disabled:checked {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "")
        icon = QIcon()
        icon.addFile(u"../file/background/9165747_send_mail_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.PushButton)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_love_2.setText("")
        self.label_idc_2.setText("")
        self.label_ok_2.setText("")
        self.label_die_2.setText("")
        self.label_omg.setText("")
        self.label_sorry.setText("")
        self.label_this.setText("")
        self.label_cry.setText("")
        self.PushButton.setText("")
    # retranslateUi

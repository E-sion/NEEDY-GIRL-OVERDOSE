import random
import time

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QTextBrowser


class Set_question:
    def set_return(self, ico, text, dir,bot:bool):  # 头像，文本，方向0
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setLayoutDirection(dir)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(45, 45))
        self.label.setText("")
        self.label.setPixmap(ico)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setStyleSheet("padding:8px;\n"
                                       "background-color: #c7e3fc;\n"
                                       "font: 13pt \"Zpix\";\n"
                                       "border-radius:15px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(text)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.widget)

    def set_return_png(self, ico, png, dir,user_or_bot):  # 头像，图片，方向
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setLayoutDirection(dir)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        if user_or_bot == 'bot':
            self.label = QtWidgets.QLabel(self.widget)
            self.label.setMaximumSize(QtCore.QSize(45, 45))
            self.label.setMinimumSize(QtCore.QSize(0, 0))
            self.label.setText("")
            self.label.setPixmap(ico)
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.horizontalLayout.addWidget(self.label)
        else:
            pass
        # 图片消息
        self.label2 = QLabel(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setPixmap(QPixmap(png))
        self.label2.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label2)
        self.verticalLayout.addWidget(self.widget)


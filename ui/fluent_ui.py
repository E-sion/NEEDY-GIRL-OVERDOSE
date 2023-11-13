# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fluent_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QListWidgetItem, QMenuBar,
                               QStatusBar, QWidget)

from qfluentwidgets import ListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ListWidget = ListWidget(self.centralwidget)
        self.ListWidget.setObjectName(u"ListWidget")
        self.ListWidget.setGeometry(QRect(270, 320, 256, 192))
        # 设置 listwidget qss样式 背景颜色为background-color: rgb(255, 170, 255);
        # self.ListWidget.setStyleSheet(u"background-color: rgb(255, 170, 255);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.ListWidget.isSortingEnabled()
        self.ListWidget.setSortingEnabled(False)
        self.ListWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

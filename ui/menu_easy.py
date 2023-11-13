# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_easy.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import PushButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(232, 92)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PushButton = PushButton(Form)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout.addWidget(self.PushButton)

        self.PushButton_3 = PushButton(Form)
        self.PushButton_3.setObjectName(u"PushButton_3")

        self.horizontalLayout.addWidget(self.PushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.PushButton_2 = PushButton(Form)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.verticalLayout.addWidget(self.PushButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u9009\u9879\u5bf9\u8bdd", None))
        self.PushButton_3.setText(QCoreApplication.translate("Form", u"\u81ea\u7531\u5bf9\u8bdd", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u91cd\u65b0\u9009\u62e9\u4ea4\u4e92\u65b9\u5f0f", None))
    # retranslateUi


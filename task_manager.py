# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(394, 369)
        font = QFont()
        font.setFamilies([u"Zpix"])
        Form.setFont(font)
        Form.setContextMenuPolicy(Qt.NoContextMenu)
        Form.setStyleSheet(u"background-color: rgb(255, 248, 255);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1, 1, 391, 364))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, -1, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"file/background/icon_status_follower.png"))

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, -1, -1, -1)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Zpix"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.change_fans = QLabel(self.widget)
        self.change_fans.setObjectName(u"change_fans")
        font2 = QFont()
        font2.setFamilies([u"Zpix"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.change_fans.setFont(font2)

        self.verticalLayout.addWidget(self.change_fans)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 6, 10, 8)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"file/background/icon_status_stress.png"))

        self.horizontalLayout_7.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 8, 12)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, -1, -1)
        self.change_pressure = QLabel(self.widget)
        self.change_pressure.setObjectName(u"change_pressure")
        font3 = QFont()
        font3.setFamilies([u"Zpix"])
        font3.setPointSize(26)
        font3.setBold(True)
        self.change_pressure.setFont(font3)
        self.change_pressure.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.change_pressure)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 6)

        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.pressure_progressBar = QProgressBar(self.widget)
        self.pressure_progressBar.setObjectName(u"pressure_progressBar")
        self.pressure_progressBar.setMinimumSize(QSize(130, 60))
        self.pressure_progressBar.setValue(24)
        self.pressure_progressBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_7.addWidget(self.pressure_progressBar)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 5)
        self.horizontalLayout_7.setStretch(2, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 6, 10, 8)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"file/background/icon_status_love.png"))

        self.horizontalLayout_6.addWidget(self.label_14)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, -1, -1, 12)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, -1, -1, -1)
        self.change_fav = QLabel(self.widget)
        self.change_fav.setObjectName(u"change_fav")
        self.change_fav.setFont(font3)
        self.change_fav.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.change_fav)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setMouseTracking(False)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 6)

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.fav_progressBar = QProgressBar(self.widget)
        self.fav_progressBar.setObjectName(u"fav_progressBar")
        self.fav_progressBar.setMinimumSize(QSize(130, 60))
        self.fav_progressBar.setValue(24)
        self.fav_progressBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_6.addWidget(self.fav_progressBar)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_6.setStretch(2, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 10, 8)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u"file/background/icon_status_yami.png"))

        self.horizontalLayout_5.addWidget(self.label_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, -1, -1, 12)
        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_24)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(6, -1, -1, -1)
        self.change_darkness = QLabel(self.widget)
        self.change_darkness.setObjectName(u"change_darkness")
        self.change_darkness.setFont(font3)
        self.change_darkness.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.change_darkness)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_26)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 5)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.darkness_progressBar = QProgressBar(self.widget)
        self.darkness_progressBar.setObjectName(u"darkness_progressBar")
        self.darkness_progressBar.setMinimumSize(QSize(130, 60))
        self.darkness_progressBar.setValue(24)
        self.darkness_progressBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_5.addWidget(self.darkness_progressBar)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(2, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4efb\u52a1\u7ba1\u7406\u5668", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7c89\u4e1d", None))
        self.change_fans.setText(QCoreApplication.translate("Form", u"1000", None))
        self.label_4.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u538b\u529b", None))
        self.change_pressure.setText(QCoreApplication.translate("Form", u"10", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"/100", None))
        self.label_14.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u597d\u611f\u5ea6", None))
        self.change_fav.setText(QCoreApplication.translate("Form", u"10", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"/100", None))
        self.label_7.setText("")
        self.label_24.setText(QCoreApplication.translate("Form", u"\u9634\u6697\u5ea6", None))
        self.change_darkness.setText(QCoreApplication.translate("Form", u"10", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"/100", None))
    # retranslateUi


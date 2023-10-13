from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QLabel, QApplication


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class tras_label:

    def set_return_label(self):

        self.label_9 = ClickableLabel(self.mywidget)

# 连接 clicked 信号到一个槽函数
#self.label_9.clicked.connect(self.on_label_clicked)

# 在你的类中添加这个槽函数
def on_label_clicked(self):

    print("Label 9 was clicked!")

#
# label = ClickableLabel("点击我")
# label.clicked.connect(lambda: print("QLabel被点击了"))
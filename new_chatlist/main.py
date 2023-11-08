from PySide6.QtCore import QRect, Qt, QSize
from PySide6.QtGui import QPixmap, QFont, QFontMetrics
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, \
    QTextBrowser, QListWidgetItem, QPushButton
from ui.new_chatlist import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.free_width = None
        self.setupUi(self)
        self.button = QPushButton(self)
        self.button.clicked.connect(self.set_item)

    def get_item(self, pic, text):
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 80, 291, 102))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFixedSize(45, 45)
        maps = QPixmap(pic).scaled(45, 45)
        self.label.setPixmap(maps)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout.addWidget(self.label)
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setText(text)

        # 自适应
        self.textBrowser.document().setTextWidth(0)
        self.free_width = self.width() - self.textBrowser.x() - 220
        self.textBrowser.setFixedSize(self.textBrowser.document().size().width() + self.free_width,
                                      self.textBrowser.document().size().height() - 50)  # 设置控件的大小为文档的大小

        self.textBrowser.setStyleSheet(u".QTextBrowser {\n"
                                       "	font: 500 12pt \"Zpix\";\n"
                                       "	color: rgb(50, 52, 154);\n"
                                       "	background-color: rgb(203, 228, 252);\n"
                                       "	border-radius: 15px;\n"
                                       "}")

        self.horizontalLayout.addWidget(self.textBrowser)

        # 设置对齐
        self.widget.setLayoutDirection(Qt.LeftToRight)  # 左边
        # self.widget.setLayoutDirection(Qt.RightToLeft)        # 右边
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setAlignment(Qt.AlignLeft)
        self.horizontalLayout.setContentsMargins(15, 15, 0, 15)
        return self.widget

    # 处理list
    def set_item(self):
        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(200, 50))  # 设置QListWidgetItem大小
        # 设置self.widget右对齐 ： Qt.AlignRight
        text = f'这是一段测试tasdhajsdhkahdjkashdkjashdkjashkashdkjashdkjashdkjasshdjkhasjkdhaskjdh'
        widget = self.get_item('../file/background/1.jpg', text)
        # 添加item
        self.listWidget.addItem(item)  # 添加item
        item.setSizeHint(widget.sizeHint())
        self.listWidget.setItemWidget(item, widget)
        self.listWidget.scrollToBottom()


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()

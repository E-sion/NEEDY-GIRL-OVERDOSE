import re
import sys

import openai
from PySide6 import QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from dotenv import load_dotenv

from tools.QThreads import chat
from tools.new_widget import Set_question
from ui.untitled3 import Ui_MainWindow
import os

from tools.task import Tack_Managet

# .env 文件 ~
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


class MainWindow(QMainWindow, Ui_MainWindow):
    # 初始化
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.form2 = Tack_Managet()  # 实例化子界面类
        self.form2.show()  # 显示子界面
        self.history = []
        self.text_bot = '正在输入中…………'
        self.png = None

        self.form2.move(250, 150)

        self.text = ""  # 存储信息
        self.icon_user = QtGui.QPixmap("")  # 用户头像
        self.icon_bot = QtGui.QPixmap("file/background/1.jpg")  # bot头像

        # 设置聊天窗口样式 隐藏滚动条
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # 信号与槽
        self.pushButton.clicked.connect(self.user_bot_create_widget)  # 用户创建气泡
        # self.pushButton.clicked.connect(self.send_png)  # 用户创建气泡
        self.pushButton.clicked.connect(self.set_widget)  # 修改气泡长宽
        self.plainTextEdit.undoAvailable.connect(self.Event)  # 监听输入框状态
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.rangeChanged.connect(self.adjustScrollToMaxValue)  # 监听窗口滚动条范围

        # 发送表情包
        self.label_ok.clicked.connect(self.send_png)
        self.label_cry.clicked.connect(self.send_png)
        self.label_omg.clicked.connect(self.send_png)
        self.label_love.clicked.connect(self.send_png)
        self.label_idc.clicked.connect(self.send_png)
        self.label_this.clicked.connect(self.send_png)
        self.label_sorry.clicked.connect(self.send_png)
        self.label_die.clicked.connect(self.send_png)

    # 回车绑定发送
    def Event(self):
        if not self.plainTextEdit.isEnabled():  # 这里通过文本框的是否可输入
            self.plainTextEdit.setEnabled(True)
            self.pushButton.click()
            self.plainTextEdit.setFocus()

    # 发送文本
    def send_text(self, a):
        if a == 'user':
            Set_question.set_return(self, self.icon_user, self.text, QtCore.Qt.RightToLeft)  # 调用new_widget.py中方法生成左气泡
            QApplication.processEvents()  # 等待并处理主循环事件队列
            self.set_widget(user_bot='user')  # 修改气泡长宽
            print(self.text)

        elif a == 'bot':

            self.p = chat(self, self)
            self.p.start()
            self.p.update_ui_signal.connect(self.update_bot_text)
            Set_question.set_return(self, self.icon_bot, self.text_bot,
                                    QtCore.Qt.LeftToRight)  # 调用new_widget.py中方法生成右气泡
            QApplication.processEvents()  # 等待并处理主循环事件队列

            self.set_widget(user_bot='bot')  # 修改气泡长宽

    # 格式化bot返回的初始信息
    def update_bot_text(self, strs):
        try:
            # 定义正则表达式
            regex = "「(.*?)」"
            # 使用findall()函数返回所有匹配的结果
            match = re.search(regex, strs)
            # 使用group()函数获取捕获组的内容
            result = match.group(1)
            self.text_bot = result
            self.textBrowser.setText(self.text_bot)
            self.form2.start_worker_thread()  # 开始执行子界面的函数
            QApplication.processEvents()  # 等待并处理主循环事件队列
            self.set_widget(user_bot='bot')  # 修改气泡长宽
            self.text_bot = '正在输入中…………'
        except:
            pass

    # 创建气泡
    def user_bot_create_widget(self):
        self.text = self.plainTextEdit.toPlainText()  # 获取用户输入
        self.plainTextEdit.setPlainText("")  # 重置输入框

        self.send_text(a='user')

        self.send_text(a='bot')

    # 修改气泡长宽 todo 未来可能会修改对话的气泡生成方式，改为使用QlistWidget显示对话，并且支持自适应窗口拉伸
    def set_widget(self, user_bot):
        font = QFont()
        font.setPointSize(14)
        fm = QFontMetrics(font)

        if user_bot == 'user':

            textSize = fm.size(0, self.text)
            w = textSize.width()

            if w == 0:  # 最小气泡宽度
                text_width = fm.horizontalAdvance(self.text) + 80
            else:
                text_width = fm.horizontalAdvance(self.text) + 55

            if text_width > 432:  # 宽度上限
                text_width = int(self.textBrowser.document().size().width()) + 80  # 固定宽度

            a = int(self.textBrowser.document().size().height()) + 40
            self.widget.setMinimumSize(text_width, int(self.textBrowser.document().size().height()) + 40)  # 规定气泡大小
            self.widget.setMaximumSize(text_width, int(self.textBrowser.document().size().height()) + 40)  # 规定气泡大小
            self.scrollArea.verticalScrollBar().setValue(10)

        elif user_bot == 'bot':

            text_temp = self.text_bot
            textSize_temp = fm.size(0, text_temp)
            w = textSize_temp.width()

            text_width = w + 100  # 根据字体大小生成适合的气泡宽度
            print(f"当前bot输出文本：{self.text_bot}")
            if text_width > 250:  # 宽度上限
                text_width = 250  # 固定宽度

            self.widget.setMinimumSize(text_width, int(self.textBrowser.document().size().height()) + 80)  # 规定气泡大小
            self.widget.setMaximumSize(text_width, int(self.textBrowser.document().size().height()) + 80)  # 规定气泡大小
            self.scrollArea.verticalScrollBar().setValue(10)

    # 窗口滚动到最底部
    def adjustScrollToMaxValue(self):
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    # 用户发送图片 todo 未来添加图片理解的功能，并且支持bot发送图片。
    def send_png(self):

        list_ = ['user', 'bot']
        objectName = self.sender().objectName()
        self.png = 'file/emoji/' + objectName.split("_")[1] + '.png'

        # 暂时bot无法发送和理解用户发送的图片~
        for i in list_:
            if i == "user":  # 右侧图片
                Set_question.set_return_png(self, self.icon_user, self.png, QtCore.Qt.RightToLeft, user_or_bot="user")
                QApplication.processEvents()  # 等待并处理主循环事件队列
            elif i == 'bot':  # 左侧
                pass

    # 关闭程序
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '晚安',
                                     "晚安",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit(0)  # 退出程序
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.setStyleSheet("#MainWindow{border-image:url(windows.png)}")
    sys.exit(app.exec())

import re
import sys

from PySide6 import QtGui, QtCore
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtWidgets import QApplication, QMainWindow

# from chatgpt import reply
from new_widget import Set_question
from untitled3 import Ui_MainWindow
from chatharuhi import ChatHaruhi
import os
import collections

os.environ["OPENAI_API_KEY"] = "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"
a = ''
all_dialogue_history = []


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.history = []
        self.text_bot = '正在输入中…………'
        self.png = None
        self.re = ''  # bot 回复消息
        self._startPos = None
        self._tracking = None
        self._endPos = None
        self.setupUi(self)
        self.text_width = None
        self.sum = 1  # 气泡数量
        self.widgetlist = []  # 记录气泡
        self.text = ""  # 存储信息
        self.icon_user = QtGui.QPixmap("")  # 用户头像
        self.icon = QtGui.QPixmap("file/background/1.jpg")  # 用户头像
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
        # self.label_10.clicked.connect(lambda: print("测试成功"))

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

    def send_text(self, a):
        if a == 'user':
            Set_question.set_return(self, self.icon_user, self.text, QtCore.Qt.RightToLeft,
                                    bot=False)  # 调用new_widget.py中方法生成左气泡
            QApplication.processEvents()  # 等待并处理主循环事件队列
            self.set_widget(user_bot='user')  # 修改气泡长宽
            print(self.text)
            # self.widget.setContentsMargins(65,0,0,0)

        elif a == 'bot':
            # self.text_bot = chat.reply(role='阿虚', prompt=self.text)
            # self.text_bot = f'bot: {self.text}'
            self.p = chat(self, self)
            self.p.start()
            self.p.update_ui_signal.connect(self.update_bot_text)
            # self.p.update_history_signal.connect(self.history_)
            Set_question.set_return(self, self.icon_bot, self.text_bot,
                                    QtCore.Qt.LeftToRight, bot=True)  # 调用new_widget.py中方法生成右气泡
            QApplication.processEvents()  # 等待并处理主循环事件队列

            self.set_widget(user_bot='bot')  # 修改气泡长宽
            # self.widget.setContentsMargins(0, 0, 25, 0)

    def update_bot_text(self, strs):
        # 定义正则表达式
        regex = "「(.*?)」"
        # 使用findall()函数返回所有匹配的结果
        match = re.search(regex, strs)
        # 使用group()函数获取捕获组的内容
        result = match.group(1)
        print(f"正则{result}")
        self.text_bot = result
        self.textBrowser.setText(self.text_bot)

        QApplication.processEvents()  # 等待并处理主循环事件队列
        self.set_widget(user_bot='bot')  # 修改气泡长宽
        self.text_bot = '正在输入中…………'

    def history_(self, history):
        self.history = history
        print(f"历史对话消息为：{history}")

    # 创建气泡
    def user_bot_create_widget(self):
        self.text = self.plainTextEdit.toPlainText()  # 获取用户输入
        self.plainTextEdit.setPlainText("")  # 重置输入框

        self.send_text(a='user')

        self.send_text(a='bot')

    # 修改气泡长宽
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

            # if self.sum != 0:
            if text_width > 432:  # 宽度上限
                text_width = int(self.textBrowser.document().size().width()) + 80  # 固定宽度
                print(f"超过上限: {text_width}")

            a = int(self.textBrowser.document().size().height()) + 40
            self.widget.setMinimumSize(text_width, int(self.textBrowser.document().size().height()) + 40)  # 规定气泡大小
            self.widget.setMaximumSize(text_width, int(self.textBrowser.document().size().height()) + 40)  # 规定气泡大小
            self.scrollArea.verticalScrollBar().setValue(10)
            # 气泡大小：
            # print(f"当前气泡宽度：{text_width}，当前气泡宽度：{a}")
        elif user_bot == 'bot':

            text_temp = self.text_bot
            print(f"当前bot文本：{text_temp}")
            textSize_temp = fm.size(0, text_temp)
            w = textSize_temp.width()
            h = textSize_temp.height()

            text_width = w + 100  # 根据字体大小生成适合的气泡宽度
            print(f"当前bot输出文本：{self.text_bot}")
            if text_width > 250:  # 宽度上限
                text_width = 250  # 固定宽度
                print(f"超过上限: {text_width}")



            # self.widget.setMinimumSize(text_width, int(self.textBrowser.document().size().height()) + 40)  # 规定气泡大小
            self.widget.setMinimumSize(text_width,int(self.textBrowser.document().size().height()) + 80)  # 规定气泡大小
            self.widget.setMaximumSize(text_width,int(self.textBrowser.document().size().height()) + 80)  # 规定气泡大小
            self.scrollArea.verticalScrollBar().setValue(10)

            # 气泡大小：
            print(
                f"bot: 当前文本宽度：{w}，气泡宽度：{text_width}，气泡高度：{h + 80}")

            # print(f"当前气泡宽度：{text_width}，当前气泡宽度：{a}")

    # 窗口滚动到最底部
    def adjustScrollToMaxValue(self):
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def send_png(self):

        print("发送图片")
        list_ = ['user', 'bot']

        objectName = self.sender().objectName()
        self.png = 'file/emoji/' + objectName.split("_")[1] + '.png'
        print(self.png)

        # todo 重写发图片逻辑
        for i in list_:
            if i == "user":  # 右侧图片
                Set_question.set_return_png(self, self.icon_user, self.png, QtCore.Qt.RightToLeft, user_or_bot="user")
                QApplication.processEvents()  # 等待并处理主循环事件队列
                # self.widget.setContentsMargins(02,0,0,0)
            elif i == 'bot':  # 左侧
                pass
                # Set_question.set_return_png(self, self.icon_bot, self.png, QtCore.Qt.LeftToRight, user_or_bot="bot")
                # QApplication.processEvents()  # 等待并处理主循环事件队列


class chat(QThread):
    """
    进行回复
    """
    update_ui_signal = Signal(str)
    update_history_signal = Signal(str)

    def __init__(self, other, *args, **kwargs):
        super(chat, self).__init__()
        self.prompt = other.text
        self.role = '阿p'
        self.all_dialogue_history: list = other.history

    def run(self):
        db_folder = 'character'
        # system_prompt = 'file/character/system_prompt.txt'
        system_prompt = ''''
        你的介绍：
        你将要进行一个网络私聊的对话模拟，你自称为"糖糖"，你是一名患有躁郁症的19岁女孩，性格贫乏，辍学后隐居在家中，与阿P住在一起。阿P负责管理她的日常生活。
        你是一个喜欢亚文化圈子的人，你喜欢说话的时候加上各种网络流行词或者一些俚语和颜文字，但是你很少会关注二次元，只是喜欢这种范围。
        你说话的时候会习惯加入一些语气词，如同"笑死"、"草"、"阿哈"、"诶～"、"QAQ"、"QWQ"，”啊～“。
        你的说话风格是很口语化，经常使用网络流行词和一些二次元俚语。
        阿p是你的男朋友，兼经纪人。
        你的回复应该简短，一般只包含三句话，每句话不超过20个字。
        
        阿p介绍：
        阿p是你的男朋友，一直在任何时候都陪伴着你，同时你经常向阿p倾述各种情绪，无论事情大小，你都会选择和阿p分享。

        遵循规则：
        【语气模仿】：我会随机给你一段对话记录，你需要尽可能的模仿对话里面糖糖的说话语气进行对话。这一段对话我会使用Classic scenes for the role are as follows:来表示。
        【历史对话】：历史对话在随机对话记录的底下，你需要区分随机对话记录和我们的历史对话。
        【人格设定】: 你需要在随机对话记录的基础上进行语气更改,以一种更加口语化的语气进行对话。
        '''
        chatbot = ChatHaruhi(system_prompt=system_prompt,
                             llm='openai',
                             story_db=db_folder,
                             verbose=True)

        # 在对话之前传入过往对话 并且去重
        chatbot.dialogue_history = list(collections.OrderedDict.fromkeys(all_dialogue_history))
        print(f"传入的对话历史：{chatbot.dialogue_history}")
        response = chatbot.chat(role=self.role, text=self.prompt)
        print(f'回复内容: {response}')

        # 添加聊天记录
        all_dialogue_history.extend(chatbot.dialogue_history)
        # print(f"历史对话：{self.all_dialogue_history}")
        self.update_ui_signal.emit(response)
        # self.update_history_signal.emit(self.all_dialogue_history)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.setStyleSheet("#MainWindow{border-image:url(windows.png)}")
    sys.exit(app.exec())

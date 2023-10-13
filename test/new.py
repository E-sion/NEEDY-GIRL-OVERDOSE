# 导入PyQt5模块
import os

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize
import sys

from chatharuhi import ChatHaruhi


# 定义聊天窗口类，继承自QWidget
class ChatWindow(QWidget):
    # 定义构造函数
    def __init__(self):
        # 调用父类的构造函数
        super().__init__()
        # 设置窗口标题和大小
        self.text_bot = None
        self.setWindowTitle("Bing聊天")
        self.resize(600, 400)
        # 创建垂直布局，并设置为窗口的布局
        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)
        # 创建列表部件，并添加到垂直布局中
        self.createListWidget()
        # 创建输入部件，并添加到垂直布局中
        self.createInputWidget()

    # 定义创建列表部件的方法
    def createListWidget(self):
        # 创建一个列表部件对象，并设置为单选模式和无边框样式
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.NoSelection)
        self.list_widget.setFrameStyle(QListWidget.NoFrame)
        # 添加列表部件到垂直布局中，并设置比例因子为1，表示占据剩余空间的全部高度
        self.v_layout.addWidget(self.list_widget, 1)

    # 定义创建输入部件的方法
    def createInputWidget(self):
        # 创建一个水平布局对象
        self.h_layout = QHBoxLayout()
        # 创建一个输入框对象，并设置提示文本和最小高度
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("请输入消息")
        self.input_box.setMinimumHeight(50)
        # 添加输入框到水平布局中，并设置比例因子为1，表示占据剩余空间的全部宽度
        self.h_layout.addWidget(self.input_box, 1)
        # 创建一个按钮对象，并设置文本和最小高度
        self.send_button = QPushButton("发送")
        self.send_button.setMinimumHeight(50)
        # 连接按钮的点击信号到发送消息的方法
        self.send_button.clicked.connect(self.send_message)
        # 添加按钮到水平布局中
        self.h_layout.addWidget(self.send_button)
        # 添加水平布局到垂直布局中
        self.v_layout.addLayout(self.h_layout)

    # 定义发送消息的方法
    def send_message(self):
        # 获取输入框中的文本内容，并去除首尾空白字符
        text = self.input_box.text().strip()
        # 如果文本内容不为空，则创建并显示一条自己发送的消息，并清空输入框中的内容
        if text:
            self.create_message_item(text, "self")
            self.input_box.clear()
            # 调用回复消息的方法，模拟对方回复的消息
            self.reply_message(text)

    # 定义回复消息的方法，接收一个文本内容作为参数
    def reply_message(self, text):
        #
        # self.text_bot = reply(role='', prompt=text)
        # print("no ero")
        # print(self.text_bot)
        os.environ["OPENAI_API_KEY"] = "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"

        all_dialogue_history = []

        db_folder = 'file/character/haruhi'
        system_prompt = 'file/character/system_prompt.txt'

        chatbot = ChatHaruhi(system_prompt=system_prompt,
                             llm='openai',
                             story_db=db_folder,
                             verbose=True)

        response = chatbot.chat(role="阿虚", text=text)

        print(f'回复内容: {response}')

        # # 根据文本内容，生成一个简单的回复内容，这里只是为了演示，可以根据需要修改或增加更多逻辑和内容
        # if text == "你好":
        #     reply = "你好，很高兴认识你。"
        # elif text == "你是谁":
        #     reply = "我是Bing，一个智能聊天机器人。"
        # elif text == "你会做什么":
        #     reply = "我会跟你聊天，还会帮你搜索网页、生成图形艺术等等。"
        # else:
        #     reply = "对不起，我不太明白你说什么。"
        # # 创建并显示一条对方发送的消息
        self.create_message_item(self.text_bot, "other")



    # 定义创建消息项的方法，接收一个文本内容和一个发送方作为参数
    def create_message_item(self, text, sender):
        # 创建一个列表项对象，并设置为自定义类型和大小
        item = QListWidgetItem()
        item.setData(Qt.UserRole, text)
        item.setSizeHint(QSize(self.list_widget.width(), 80))
        # 将列表项添加到列表部件中
        self.list_widget.addItem(item)
        # 创建一个标签对象，并设置为列表项的子部件
        label = QLabel(self.list_widget)
        label.setText(text)
        label.setWordWrap(True)
        label.setFont(QFont("Arial", 14))
        # 根据发送方，设置标签的对齐方式和背景颜色
        if sender == "self":
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            label.setStyleSheet("background-color: lightblue; margin: 10px; border-radius: 10px;")
        else:
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            label.setStyleSheet("background-color: lightgreen; margin: 10px; border-radius: 10px;")
        # 设置列表项的子部件为标签
        self.list_widget.setItemWidget(item, label)
        # 滚动列表部件到最底部，以显示最新的消息
        self.list_widget.scrollToBottom()

# 创建应用对象
app = QApplication(sys.argv)
# 创建聊天窗口对象
window = ChatWindow()
# 显示聊天窗口
window.show()
# 进入应用的事件循环
sys.exit(app.exec_())

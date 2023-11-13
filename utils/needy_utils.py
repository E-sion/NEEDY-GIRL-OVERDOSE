import logging
import re

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFontMetrics, QPixmap, QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextBrowser, QApplication
from qfluentwidgets import PushButton


# 设置对话列表中单条对话widget的格式
def message_item_type(self, ico, text, png=''):
    self.widget = QWidget(self)
    self.widget.setObjectName(u"widget")
    self.widget.setGeometry(QRect(20, 80, 291, 102))
    self.horizontalLayout = QHBoxLayout(self.widget)
    self.horizontalLayout.setObjectName(u"horizontalLayout")
    self.textBrowser = QTextBrowser(self.widget)
    self.textBrowser.setObjectName(u"textBrowser")

    # 处理头像
    if ico != '':
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFixedSize(45, 45)
        maps = QPixmap(ico).scaled(45, 45)
        self.label.setPixmap(maps)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout.addWidget(self.label)

    # 空余空间 40为头像的固定宽度
    self.free_width = (self.windows_width - 40) / 2

    # 文本输入框为文字时
    if png == '':
        # 新建字体
        font = QFont()
        font.setPointSize(14)
        fm = QFontMetrics(font)
        wrap_text = self.wrap_text(text, self.free_width, font)
        # 比较蠢的方法来实现换行：首先把原字符串进行切割处理，让每一行的宽度都等于设置的最大宽度
        # 随后再把处理好的字符串计算行数，已知一行占高25，相乘以下就可以让输入框适应字符串了。
        lines_number = wrap_text.count('\n') + 1
        text_width = fm.horizontalAdvance(wrap_text)
        text_height = 25 * lines_number

        # 设置文本
        self.textBrowser.setText(wrap_text)

        # 设置自适应框
        if text_width == 0:  # 设置最小宽度
            self.textBrowser.setFixedSize(self.windows_width - 40 / 5,
                                          text_height)

        elif text_width >= self.free_width:  # 设置最大数值
            self.textBrowser.setFixedSize(self.free_width - 27,
                                          text_height)
        else:
            self.textBrowser.setFixedSize(text_width + 3,
                                          text_height + 5)

        self.logger.info('文本的宽度: %s ，文本的高度：%s', text_width, text_height)

        # todo 美化qss
        self.textBrowser.setStyleSheet(u".QTextBrowser {\n"
                                       "	font: 500 12pt \"Zpix\";\n"
                                       "	color: rgb(50, 52, 154);\n"
                                       "	background-color: rgb(203, 228, 252);\n"
                                       "	border-radius: 15px;\n"
                                       "}")

    else:
        self.textBrowser.setHtml(f"""<img src="{png}"/>""")
        # 把图片的长度宽度设置为textbrowser的大小
        self.textBrowser.setFixedSize(60, 60)

        self.textBrowser.setStyleSheet(u".QTextBrowser {\n"
                                       "	background-color: transparent;\n"
                                       "	border-radius: 15px;\n"
                                       "}")

    # 使用logger来输出信息
    self.logger.info('当前窗口宽度: %s', self.windows_width)
    self.logger.info('空余宽度: %s', self.free_width)

    self.horizontalLayout.addWidget(self.textBrowser)

    # 取消水平滚动条
    self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # 取消垂直滚动条
    self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    self.horizontalLayout.setSpacing(10)
    self.horizontalLayout.setAlignment(Qt.AlignLeft)
    self.horizontalLayout.setContentsMargins(0, 10, 0, 10)

    # 禁止编辑
    self.textBrowser.setReadOnly(True)
    return self.widget


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
        self.text_bot = '少女祈祷中……'
    except:
        pass


# 生成对话选项
def get_choose_item(self):
    pass


def set_logger(self):
    # 创建一个logger
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.INFO)
    # 创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # 给logger添加handler
    self.logger.addHandler(ch)



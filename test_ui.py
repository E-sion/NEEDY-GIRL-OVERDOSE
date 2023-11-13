from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, \
    QListWidgetItem

from tools.QThreads import chat
from tools.easy_menu import menu
from tools.haruhi_needy import EventMaster, ChatMaster, ImageMaster, events, memory_pool, image_pool, agent
from tools.new_widget import Set_question
from ui.fluent_ui import Ui_MainWindow
from utils.needy_utils import message_item_type, set_logger


class Mainwin(QMainWindow, Ui_MainWindow):
    """
    todo 预计添加的功能
    1. PASS 显示数值子窗口
    2. DONE 判断用户输入与bot回复，生成不同的list item
    3. DONE 发送表情包
    4. PASS 回车绑定输入
    5. PASS 初始化bot的输出内容，添加输入中的内容
    6. PASS 用户关闭窗口提示
    7. DONE 用户发送图片
    8. PASS bot发送图片
    9. DONE 修改糖糖头像的位置，在偏左一些
    10. DONE 精简美化一下代码格式
    11. 处理背景图片
    12. DONE 添加线程~
    13. DONE 移动一下choose list的位置
    14. DONE对话之后禁止pushbutton点击,回复之后再允许点击
    """

    def __init__(self):
        super(Mainwin, self).__init__()
        # 初始化
        self.user_choose_text = ''
        self.choose_text = ''
        self.time_event = 0
        self.time_emoji = 1
        self.now_enent = None
        self.bot_text = ''
        self.user_text = ''
        self.windows_width = 0
        self.windows_height = 0
        self.setupUi(self)
        self.text_bot = ''
        self.text_user = ''
        # 设置窗口的大小
        self.resize(400, 600)
        # 设置窗口的标题
        self.setWindowTitle('AI糖糖')
        # 设置窗口图标
        self.setWindowIcon(QtGui.QIcon('file/background/1.jpg'))

        # 设置中心控件
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        # 默认添加list显示作为消息显示框
        self.verticalLayout.addWidget(self.ListWidget)

        # 添加中心控件
        self.setCentralWidget(self.centralwidget)

        # logger
        set_logger(self)

        # todo 调用添加中心控件 更改调用方式
        self.emoji_line()

        # 按钮触发添加列表内容
        # self.PushButton.clicked.connect(self.user_bot_create_widget)

        self.event_master = EventMaster(events)
        self.chat_master = ChatMaster(memory_pool)
        self.image_master = ImageMaster(image_pool)
        self.chat_master.set_image_master(self.image_master)
        self.event_master.set_image_master(self.image_master)

        self.menu_ui = menu()
        self.menu_ui.show()
        self.menu_ui.PushButton.clicked.connect(self.event_choose)
        self.menu_ui.PushButton_3.clicked.connect(self.chat_master_repaly)
        # 设置menu_ui窗口的位置在本窗口的右边
        self.menu_ui.move(self.x() + self.width(), self.y())

        # 试用线程
        self.bot_thread = chat(self, self)

    # 获取实时窗口大小
    def resizeEvent(self, event):
        # 获取新的窗口大小
        new_size = event.size()
        # 设置对话框大小变化
        self.windows_width = new_size.width()
        self.windows_height = new_size.height()

    # 为对话列表新加对话列表
    def send_message_item(self, user_bot):
        user_text = str(self.user_text)

        if user_text == '':
            return

        self.logger.info('用户输入: %s', user_text)

        # 默认不添加图片
        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(200, 50))  # 设置QListWidgetItem大小
        if user_bot == 'bot':
            widget = message_item_type(self, 'file/background/1.jpg', self.bot_text)
            widget.setLayoutDirection(Qt.LeftToRight)  # 左边
        elif user_bot == 'user':
            widget = message_item_type(self, '', self.user_text)
            widget.setLayoutDirection(Qt.RightToLeft)  # 右边

        # 添加item
        self.ListWidget.addItem(item)  # 添加item
        item.setSizeHint(widget.sizeHint())
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)  # 禁止点击
        self.ListWidget.setItemWidget(item, widget)
        self.ListWidget.scrollToBottom()

    # 用户发送文本
    # 选项回复模式
    def choose_user_create_widget(self):
        self.user_text = self.LineEdit_choose.text()  # 获取用户输入
        self.LineEdit_choose.setText('')  # 重置输入框
        # self.bot_text = self.chat_master.get_repaly(self.user_text)  # 获取回复
        # 线程处理回复
        self.bot_thread.start()
        self.bot_thread.update_ui_signal.connect(self.update_bot_text)

        self.send_message_item(user_bot='user')
        self.send_message_item(user_bot='bot')
        # 获取bot回复

    # 自由对话模式
    def emoji_user_create_widget(self):
        self.user_text = self.LineEdit_emoji.text()  # 获取用户输入
        if self.user_text == '':
            return
        self.LineEdit_emoji.setText('')  # 重置输入框

        self.bot_text = self.chat_master.get_repaly(self.user_text)  # 获取回复

        self.send_message_item(user_bot='user')
        self.send_message_item(user_bot='bot')

    # 线程化bot回复
    def update_bot_text(self, response):
        # self.bot_text = '正在输入中…………'
        self.bot_text = response
        if self.bot_text != '':
            self.send_message_item(user_bot='bot')

    # 调用生成emoji和输入框
    def emoji_line(self):
        Set_question.return_emoji_line(self)

        # 发送表情包
        self.label_ok.button_clicked_signal.connect(self.user_send_png)
        self.label_cry.button_clicked_signal.connect(self.user_send_png)
        self.label_omg.button_clicked_signal.connect(self.user_send_png)
        self.label_love.button_clicked_signal.connect(self.user_send_png)
        self.label_idc.button_clicked_signal.connect(self.user_send_png)
        self.label_this.button_clicked_signal.connect(self.user_send_png)
        self.label_sorry.button_clicked_signal.connect(self.user_send_png)
        self.label_die.button_clicked_signal.connect(self.user_send_png)
        # 设置控件

    # 生成选项列表
    def choose_line(self):
        Set_question.return_choose_list(self)

    def return_choose_item(self):
        # 默认不添加图片
        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(200, 50))  # 设置QListWidgetItem大小

        widget = message_item_type(self, 'file/background/1.jpg', self.choose_text)
        widget.setLayoutDirection(Qt.LeftToRight)  # 左边

        # 添加item
        self.ListWidget.addItem(item)  # 添加item
        item.setSizeHint(widget.sizeHint())
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)  # 禁止点击
        self.ListWidget.setItemWidget(item, widget)
        self.ListWidget.scrollToBottom()

    # 用户发送表情包
    def user_send_png(self):
        # 获取图片名称
        objectName = self.sender().objectName()
        png = 'file/emoji/' + objectName.split("_")[1] + '.png'
        # 发送图片
        self.logger.info('用户发送表情包: %s', png)

        widget = message_item_type(self, '', 'a ', png=png)
        widget.setLayoutDirection(Qt.RightToLeft)

        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(200, 50))  # 设置QListWidgetItem大小
        # 添加item
        self.ListWidget.addItem(item)  # 添加item
        item.setSizeHint(widget.sizeHint())
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)  # 禁止点击
        self.ListWidget.setItemWidget(item, widget)
        self.ListWidget.scrollToBottom()

    # bot发送表情包
    def bot_send_png(self):
        # todo 正则或者其他方式获取到bot回复中的图片名称，再进行匹配，之后就是发送图片了
        # 以后再来写吧
        widget = message_item_type(self, 'file/background/1.jpg', '', png='')
        widget.setLayoutDirection(Qt.LeftToRight)

    # 切割文本实现自动换行
    def wrap_text(self, text, width, font):
        words = list(text)
        wrapped_text = ''
        line = ''
        time = 0
        for word in words:
            time += 1
            if QFontMetrics(font).horizontalAdvance(line + word + ' ') <= width:
                line += word + ''
            elif time == 1:
                wrapped_text += line + ''
                line = word + ''
            else:
                wrapped_text += line + '\n'
                line = word + ''
        wrapped_text += line

        return wrapped_text

    def event_choose(self):
        if self.time_event == 0:
            self.choose_line()
            # 取消显示 self.LineEdit_choose和self.PushButton_choose控件
            self.verticalLayout.removeWidget(self.PushButton_choose)
            self.verticalLayout.removeWidget(self.LineEdit_choose)

            self.PushButton_choose.deleteLater()
            self.LineEdit_choose.deleteLater()

        # 删除控件
        if self.time_emoji != 0:
            # 删除horizontalLayout_4里面的所有
            for i in range(self.horizontalLayout_4.count()):
                self.horizontalLayout_4.itemAt(i).widget().deleteLater()

            for i in range(self.horizontalLayout_5.count()):
                self.horizontalLayout_5.itemAt(i).widget().deleteLater()

            self.verticalLayout.removeWidget(self.PushButton_emoji)
            self.verticalLayout.removeWidget(self.LineEdit_emoji)

            self.PushButton_emoji.deleteLater()
            self.LineEdit_emoji.deleteLater()
            self.time_emoji = 0

        self.ListWidget_choose.clear()

        self.now_enent = self.event_master.get_random_event(agent)
        self.choose_text = self.now_enent["prefix"]

        # self.send_message_item(user_bot='choose')
        # 处理生成对话item
        self.return_choose_item()

        # 生成选项,以及处理回复
        options = self.now_enent["options"]

        for i, option in enumerate(options):
            text = option["user"]
            PushButton = QPushButton(f"{i + 1}. 阿p：{text}")
            # 试试把用户的text也新添加一个列表
            self.user_choose_text = text
            PushButton.setObjectName(str(i))
            PushButton.clicked.connect(self.replay)
            PushButton_item = QListWidgetItem()
            self.ListWidget_choose.addItem(PushButton_item)
            self.ListWidget_choose.setItemWidget(PushButton_item, PushButton)
        self.time_event += 1

        # 按钮发送对话
        # self.PushButton_choose.clicked.connect(self.choose_user_create_widget)

    def replay(self, text):

        # 获取事件名称
        objectName = self.sender().objectName()
        # 清理列表
        self.ListWidget_choose.clear()

        options = self.now_enent["options"]
        self.choose_text = options[int(objectName)]["reply"]
        # 用户对话item
        self.user_text = options[int(objectName)]["user"]
        self.send_message_item(user_bot='user')
        # 添加item 进行回复
        QtCore.QTimer.singleShot(600, self.return_choose_item)

        # 继续显示其他的选项
        QtCore.QTimer.singleShot(3000, self.event_choose)

    def chat_master_repaly(self):
        if self.time_emoji == 0:
            self.emoji_line()
        if self.time_event != 0:
            self.ListWidget_choose.clear()
            # 取消显示ListWidget_choose
            self.verticalLayout.removeWidget(self.ListWidget_choose)
            # self.verticalLayout.removeWidget(self.PushButton_choose)
            # self.verticalLayout.removeWidget(self.LineEdit_choose)

            self.ListWidget_choose.deleteLater()
            # self.PushButton_choose.deleteLater()
            # self.LineEdit_choose.deleteLater()
            self.time_event = 0

        self.time_emoji += 1

        # 发送按钮进行对话
        self.PushButton_emoji.clicked.connect(self.emoji_user_create_widget)

        # 提示一下
        # self.chat_master.get_repaly(self.user_text)

        # 重写关闭窗口,当本窗口关闭的时候也会关闭其他窗口

    def closeEvent(self, event):
        try:
            reply = self.menu_ui.close()
            if reply == 1:
                event.accept()
            else:
                event.ignore()
        except:
            pass


if __name__ == '__main__':
    app = QApplication([])
    win = Mainwin()
    win.show()
    app.exec()

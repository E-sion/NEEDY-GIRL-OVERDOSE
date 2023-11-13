"""整合线程"""
import os
import pickle
from PySide6.QtCore import QThread, Signal
import collections

import chromadb.migrations.embeddings_queue

from tools.haruhi_needy import ChatMaster, memory_pool


# bot回复
class chat(QThread):
    """
    进行回复
    """
    update_ui_signal = Signal(str)

    def __init__(self, main, *args, **kwargs):
        super(chat, self).__init__()
        self.user_text = main.user_text
        self.chat_master = ChatMaster(memory_pool)

    def run(self):
        # 长时间操作~
        response = self.chat_master.get_repaly(self.user_text)  # 获取回复

        self.update_ui_signal.emit(response)


# 数值窗口刷新
class WorkerThread(QThread):
    progress_updated = Signal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        # 长时间操作~
        list_value = self.get_history()
        if list_value is not None or list_value != '':
            # 传递信息
            self.progress_updated.emit(list_value)
        else:
            pass

    def get_history(self):
        # 读取本地历史对话（如果有）
        if os.path.exists('file/chat_history/chat_history.pkl'):
            with open('file/chat_history/chat_history.pkl', 'rb') as f:
                all_dialogue_history = pickle.load(f)

            # 添加限制
            if len(all_dialogue_history) % 2 == 0:
                print(len(all_dialogue_history))
                # 历史记录传递给chatgpt，获得格式化后的数值
                re_temp = get_vale(all_dialogue_history)
                print("re_temp: ", re_temp)
                value: list = re_(re_temp)
                # 处理数值
                return value
            else:
                return
        else:
            return


class Windows_chat_widet(QThread):
    progress_updated = Signal(list)

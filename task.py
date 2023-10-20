import os
import pickle

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget, QApplication, QProgressBar, QLabel, QMainWindow

from get_value_gpt import get_vale, re_
from task_manager import Ui_Form


# 更新线程
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
                # print(f' 本地聊天记忆库：{all_dialogue_history}\n')

            # 添加限制，避免频繁回复
            if len(all_dialogue_history) % 3 == 0:
                # 历史记录传递给chatgpt，获得数值
                re_temp = get_vale(all_dialogue_history)
                print("re_temp: ", re_temp)
                value: list = re_(re_temp)
                print("value: ", value)
                # 处理数值
                return value
            else:
                return
        else:
            return


class Tack_Managet(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.setupUi(self)
        # 开启线程
        self.start_worker_thread()

    def get_history(self):
        # 读取本地历史对话（如果有）
        if os.path.exists('file/chat_history/chat_history.pkl'):
            with open('file/chat_history/chat_history.pkl', 'rb') as f:
                all_dialogue_history = pickle.load(f)
                # print(f' 本地聊天记忆库：{all_dialogue_history}\n')

            # 添加限制，避免频繁回复
            if len(all_dialogue_history) % 3 == 0:
                # 历史记录传递给chatgpt，获得数值
                re_temp = get_vale(all_dialogue_history)
                print("re_temp: ", re_temp)
                value: list = re_(re_temp)
                print("value: ", value)
                # 处理数值
                self.set_progressbar(value)
            else:
                return
        else:
            return

    def set_progressbar(self, progress_values: list):
        """
        设置进度条数值,同时设置label的数值
        """
        if progress_values == [] or progress_values is None or progress_values == "":
            pass
        else:
            print(f'传递内容：{progress_values}')
            # 尝试获取当前的总数值 all_progress_values 。如果没有则在本地创建一个文件用来储存总数值，并且重置总数值的值都为0，0，0。如果有本地总数值文件，则读取将总数值的值进行更新处理。
            if os.path.exists('file/all_progress_values.pkl'):
                # 读取本地总数值文件
                with open('file/all_progress_values.pkl', 'rb') as f:
                    all_progress_values = pickle.load(f)
            else:
                # 创建本地总数值文件，并初始化为[0, 0, 0]
                all_progress_values = [0, 0, 0]
                with open('file/all_progress_values.pkl', 'wb') as f:
                    pickle.dump(all_progress_values, f)

            # 对总数值进行处理后，进行储存到本地。
            # 将传递过来的progress_values与本地总数值相加，得到更新后的总数值
            all_progress_values = [x + y for x, y in zip(all_progress_values, progress_values)]
            print(f'更新后内容：{all_progress_values}')

            # 处理第一个列表，在总数值的基础上加上传递过来的第一个列表代表的值，并且设置pressure_progressBar的
            # 设置label的值为总数值。
            self.change_pressure.setText(str(all_progress_values[0]))
            # 设置进度条的值为总数值，处理负数情况
            if progress_values[0] <= 0:
                self.pressure_progressBar.setValue(0)
            else:
                self.pressure_progressBar.setValue(all_progress_values[0])

            # 处理第二个列表,操作和第一个列表一样
            # 设置label的值为总数值。
            self.change_fav.setText(str(all_progress_values[1]))
            # 设置进度条的值为总数值
            if progress_values[1] <= 0:
                self.fav_progressBar.setValue(0)
            else:
                self.fav_progressBar.setValue(all_progress_values[1])

            # 处理第三个列表,操作和第一个列表一样
            # 设置label的值为总数值。
            self.change_darkness.setText(str(all_progress_values[2]))
            # 设置进度条的值为总数值
            if progress_values[2] <= 0:
                self.darkness_progressBar.setValue(0)
            else:
                self.darkness_progressBar.setValue(all_progress_values[2])

    def open(self):
        '''
        显示主窗口界面
        '''
        self.show()

    # 使用线程更新
    def start_worker_thread(self):
        # 接收内容，更新
        try:
            self.thread = WorkerThread()
            self.thread.progress_updated.connect(self.set_progressbar)
            self.thread.start()
        except:
            pass


if __name__ == '__main__':
    app = QApplication([])
    window = Tack_Managet()
    window.show()
    app.exec()

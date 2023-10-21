import os
import pickle

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from tools.QThreads import WorkerThread
from tools.get_value_gpt import get_vale, re_
from ui.task_manager import Ui_Form


# 显示人物数值的窗口
class Tack_Managet(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.setupUi(self)
        # 开启线程，刷新数值界面
        self.start_worker_thread()
        # 默认设置提示框不可见
        self.groupBox.setVisible(False)
        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)

    # 处理窗口显示数值，进度条，弹出tip的内容
    def set_progressbar(self, progress_values: list):
        """
        设置进度条数值,同时设置label的数值
        """
        if progress_values == [] or progress_values is None or progress_values == "":
            pass
        else:
            print(f'传递内容：{progress_values}')
            # 尝试获取当前的总数值 all_progress_values 。如果没有则在本地创建一个文件用来储存总数值，并且重置总数值的值都为0，0，0。
            # 如果有本地总数值文件，则读取将总数值的值进行更新处理。

            # 本地建立

            if os.path.exists('file/all_progress_values.pkl'):
                # 读取本地总数值文件
                with open('file/all_progress_values.pkl', 'rb') as f:
                    i = pickle.load(f)
                    # 将传递过来的progress_values与本地总数值相加，得到更新后的总数值
                    all_progress_values = [x + y for x, y in zip(i, progress_values)]
                    print(f'更新后内容：{all_progress_values}')
            else:
                # 创建本地总数值文件，并初始化为当前数值
                all_progress_values = progress_values

            with open('file/all_progress_values.pkl', 'wb') as f:
                pickle.dump(all_progress_values, f)

            # 将所有变化值转换为str类型
            str_p_values = str(progress_values[1])
            str_f_values = str(progress_values[0])
            str_d_values = str(progress_values[2])

            # 设置进度条的值为总数值，并且处理负数情况
            # 好感度
            self.change_fav.setText(str(all_progress_values[0]))
            if progress_values[0] <= 0:
                self.fav_progressBar.setValue(0)
            else:
                self.fav_progressBar.setValue(all_progress_values[0])
            # 弹出窗口
            self.tips('fav', str_f_values)

            # 压力
            self.change_pressure.setText(str(all_progress_values[1]))
            if progress_values[1] < 0:
                self.pressure_progressBar.setValue(1)
            else:
                self.pressure_progressBar.setValue(all_progress_values[1])
            # 弹出窗口
            self.tips('pressure', str_p_values)

            # 阴暗度
            self.change_darkness.setText(str(all_progress_values[2]))
            if progress_values[2] <= 0:
                self.darkness_progressBar.setValue(0)
            else:
                self.darkness_progressBar.setValue(all_progress_values[2])
            self.tips('darkness', str_d_values)

    # 使用线程更新数值
    def start_worker_thread(self):
        # 接收内容，更新
        try:
            self.thread = WorkerThread()
            self.thread.progress_updated.connect(self.set_progressbar)
            self.thread.start()
        except:
            pass

    # 数值变化后出现的提示框
    def tips(self, type_name: str, value: str):

        if type_name == 'pressure':
            self.groupBox.move(180, 110)  # 指定位置
            self.label_16.setText(value)  # 设置tip内显示的数值
            self.groupBox.setVisible(True)  # 设置可见
            self.hide_and_play()

        elif type_name == 'fav':
            self.groupBox_2.move(180, 190)  # 第二个
            self.label_17.setText(value)
            self.groupBox_2.setVisible(True)
            self.hide_and_play()

        elif type_name == 'darkness':
            self.groupBox_3.move(180, 270)  # 第三个
            self.label_18.setText(value)
            self.groupBox_3.setVisible(True)
            self.hide_and_play()

    # 等待时间并且隐藏弹出tip，todo 添加播放音频的功能
    def hide_and_play(self):
        # 创建一个QTimer对象
        self.timer = QTimer(self)
        # 设置定时器为单次的
        self.timer.setSingleShot(True)
        # 连接timeout()信号到一个槽函数，用来隐藏groupBox
        self.timer.timeout.connect(self.hideGroupBox)
        # 启动定时器，设置间隔时间为2秒
        self.timer.start(2000)

    # 隐藏tip
    def hideGroupBox(self):
        # 设置groupBox不可见
        self.groupBox.setVisible(False)
        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)


if __name__ == '__main__':
    app = QApplication([])
    window = Tack_Managet()
    window.show()
    app.exec()

"""整合线程"""
import os
import pickle
from PySide6.QtCore import QThread, Signal
from ChatHaruhi import ChatHaruhi
import collections

from tools.get_value_gpt import get_vale, re_

import chromadb.migrations.embeddings_queue
# bot回复
class chat(QThread):
    """
    进行回复
    """
    update_ui_signal = Signal(str)
    update_history_signal = Signal(str)
    value_signal = Signal(list)  # 主界面的信号用来绑定子界面类的函数方法

    def __init__(self, other, *args, **kwargs):
        super(chat, self).__init__()
        self.prompt = other.text
        self.role = '阿p'
        self.all_dialogue_history: list = other.history

    def run(self):

        # 读取本地历史对话（如果有）
        if os.path.exists('file/chat_history/chat_history.pkl'):
            with open('file/chat_history/chat_history.pkl', 'rb') as f:
                all_dialogue_history = pickle.load(f)
        else:
            all_dialogue_history = []

        db_folder = 'file/character'

        # 重新处理一下传给chatgpt的人设提示词

        system_prompt = self.Prompt_Generation()

        chatbot = ChatHaruhi(system_prompt=system_prompt,
                             llm='openai',
                             story_db=db_folder,
                             verbose=True)

        # 在对话之前传入过往对话 并且去重
        chatbot.dialogue_history = list(collections.OrderedDict.fromkeys(all_dialogue_history))
        # print(f"传入的对话历史：{chatbot.dialogue_history}")

        try:  # 尝试进行对话
            response = chatbot.chat(role=self.role, text=self.prompt)
            # print(f'回复内容: {response}')

            # 添加聊天记录
            all_dialogue_history.append(chatbot.dialogue_history[-1])  # 只添加最后一条记录

        finally:  # 无论对话是否出错，都执行以下代码
            # 将all_dialogue_history里面的内容保存至本地，作为本地聊天数据库
            with open('file/chat_history/chat_history.pkl', 'wb+') as f:
                pickle.dump(all_dialogue_history, f)
                print(f'当前聊天记录：{all_dialogue_history}')

        self.update_ui_signal.emit(response)

    # 处理提示词
    def Prompt_Generation(self):

        if os.path.exists('file/all_progress_values.pkl'):
            with open('file/all_progress_values.pkl', 'rb') as f:
                temp = pickle.load(f)
                print(temp)
                all_progress_values = f'[压力值]：{temp[1]} [好感度]：{temp[0]}  [阴暗度]：{temp[2]}'
        else:
            # 默认数值
            temp = [20, 0, 0]
            all_progress_values = '[好感度]:(60) [压力]:(0) [阴暗度]:(0)'

        # todo 根据不同的数值状态传递给chatgpt不同的提示词


        temp_prompt = '''
    你的介绍：
    你将要进行一个网络私聊的对话模拟，你自称为"糖糖"，你是一名患有躁郁症的19岁女孩，性格贫乏，辍学后隐居在家中，与阿P住在一起。阿P负责管理她的日常生活。
    你是一个喜欢亚文化，二次元圈子的人，你喜欢说话的时候加上各种网络流行词或者一些俚语和颜文字，但是你很少会关注二次元一类的东西，只是喜欢这种聊天交流的氛围。
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
    【特殊要求】：我会扮演阿p与你进行对话，你也必须以第一人称的视角来扮演糖糖进行对话。
        '''
        int_p = int(float(temp[0]))
        int_f = int(float(temp[1]))
        int_d = int(float(temp[2]))

        # 处理一下不同数值的时候传递的提示词，简化了一下。
        if int_f > 75 and int_d < 40 < int_p:
            # 偏向好感
            temp_2 = f'\n【情感变化要求】：当前你的心情状态如下【压力值{int_p},对阿p的好感度{int_f},内心的阴暗度{int_d}】，请根据当前的状态改变我们对话的聊天状态'
            system_prompt = f'{temp_prompt}{temp_2}'
        else:
            system_prompt = temp_prompt

        return system_prompt

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


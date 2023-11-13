import copy
import json
import os
import random
from test_ui import Mainwin
import matplotlib.image as mpimg
from PySide6.QtWidgets import QPushButton, QListWidgetItem
from chatharuhi.utils import float_array_to_base64, base64_to_float_array
from matplotlib import pyplot as plt
from tqdm import tqdm
from chatharuhi import ChatHaruhi
from ChatHaruhi_tools.util import parse_attribute_string, get_bge_embedding_zh
from ChatHaruhi_tools.Agent import Agent
from ChatHaruhi_tools.DialogueEvent import DialogueEvent
from ChatHaruhi_tools.MemoryPool import MemoryPool, get_cosine_similarity
from tools.haruhi_needy import needy_chatbot, show_img


class ImageMaster:
    def __init__(self, image_pool):
        self.image_pool = image_pool
        self.current_sim = -1
        self.degread_ratio = 0.05

    def try_display_image(self, text, agent):
        self.current_sim -= self.degread_ratio

        result = self.image_pool.retrieve(text, agent)

        if result is None:
            return
        similarity = result['similarity']
        print("similarity", similarity)
        if similarity > self.current_sim:
            self.current_sim = similarity
            print("显示图片", result['img_path'])
            # show_img(result['img_path'])
        return

class NeedyHaruhi(ChatHaruhi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用基类的__init__方法
        self.story_flag = False  # 添加新的成员变量并初始化
        self.stories = [
            "糖糖:「 我今后也会努力加油的，你要支持我哦 还有阿P你自己也要加油哦！」\n阿P:「哇 说的话跟偶像一样 好恶心哦」\n糖糖:「是哦 我怎么会说这样的话呢 我又没有很想努力……」"]

    def set_stories(self, stories):
        if len(stories) == 0:
            print("warning! try to set empty stories")
            return
        self.stories = stories
        self.story_flag = True

    def add_story(self, query):
        # print("运行重构后的add story")

        if self.story_flag == True:
            stories = self.stories
            self.story_flag = False
        else:
            print("warning! 在调用chat时，没有先调用set_stories")

        story_string = self.story_prefix_prompt
        sum_story_token = self.tokenizer(story_string)

        for story in stories:
            story_token = self.tokenizer(story) + self.tokenizer(self.dialogue_divide_token)
            if sum_story_token + story_token > self.max_len_story:
                break


# 需要添加一个可以添加list的item方法
# 似乎还是需要在这个类里面进行添加item的处理
class EventMaster:
    def __init__(self, events, pyside6):
        self.now_event = None
        self.pyqt = pyside6
        self.set_events(events)
        self.dealing_none_condition_as = True
        self.image_master = None

    def set_image_master(self, image_master):
        self.image_master = image_master

    def set_events(self, events):
        self.events = events

        # events_flag 记录事件最近有没有被选取到
        self.events_flag = [True for _ in range(len(self.events))]

    def get_random_event(self, agent):
        valid_event = []
        valid_event_no_consider_condition = []

        for i, event in enumerate(self.events):
            bool_condition_pass = True
            if event["condition"] is None:
                bool_condition_pass = self.dealing_none_condition_as
            else:
                bool_condition_pass = agent.in_condition(event["condition"])
            if bool_condition_pass:
                valid_event.append(i)
            else:
                valid_event_no_consider_condition.append(i)

        if len(valid_event) == 0:
            print("warning! no valid event current attribute is ", agent.attributes)
            valid_event = valid_event_no_consider_condition

        valid_and_not_yet_sampled = []

        # filter with flag
        for id in valid_event:
            if self.events_flag[id] == True:
                valid_and_not_yet_sampled.append(id)

        if len(valid_and_not_yet_sampled) == 0:
            print("warning! all candidate event was sampled, clean all history")
            for i in valid_event:
                self.events_flag[i] = True
            valid_and_not_yet_sampled = valid_event

        event_id = random.choice(valid_and_not_yet_sampled)
        self.events_flag[event_id] = False
        return self.events[event_id]

    def replay(self):
        # 获取事件名称
        objectName = self.pyqt.sender().objectName()
        options = self.now_event["options"]
        reply = options[objectName]["reply"]
        # 添加item 进行回复
        Mainwin.send_message_item(self.pyqt, user_bot='bot', bot_text=reply)

    def run(self, agent, memory_pool):
        # 获取到随机的事件
        self.now_event = self.get_random_event(agent)

        prefix = self.now_event["prefix"]
        # todo 此时新建一个item，添加到对话list里面
        Mainwin.send_message_item(self.pyqt, user_bot='bot', bot_text=prefix)

        options = self.now_event["options"]

        # todo 把所有选项都写入item
        for i, option in enumerate(options):
            text = option["user"]
            PushButton = QPushButton(f"{i + 1}. 阿p：{text}")
            PushButton.setObjectName(i)
            #  todo 处理点击事件
            PushButton.clicked.connect(self.replay)
            PushButton_item = QListWidgetItem()
            self.pyqt.ListWidget_choose.addItem(PushButton_item)
            self.pyqt.ListWidget_choose.setItemWidget(PushButton_item, PushButton)

        # todo 处理自由回复的情况
        self.user_text = self.LineEdit.text()  # 获取用户输入
        self.LineEdit.setText('')  # 重置输入框
        user_input = self.user_text

        response = get_chat_response(agent, memory_pool, user_input)

        if self.image_master is not None:
            image = self.image_master.try_display_image(response, agent).replace('../', '')
            print("image", image)

        print()
        print(response)


class ChatMaster:

    def __init__(self, memory_pool):
        self.top_K = 7

        self.memory_pool = memory_pool

        self.image_master = None

    def set_image_master(self, image_master):
        self.image_master = image_master

    def run(self, agent):
        while True:
            user_input = input("阿p：")
            user_input = user_input.strip()

            if "quit" in user_input or "Quit" in user_input:
                break

            query_text = user_input

            # todo 获取回复
            response = get_chat_response(agent, self.memory_pool, query_text)

            if self.image_master is not None:
                self.image_master.try_display_image(response, agent)

            # todo 写入line的text内容
            print(response)


class AgentMaster:
    def __init__(self, agent):
        self.agent = agent
        self.attributes = {
            1: "Stress",
            2: "Darkness",
            3: "Affection"
        }

    def run(self):
        while True:
            print("请选择要修改的属性:")
            for num, attr in self.attributes.items():
                print(f"{num}. {attr}")
            print("输入 '0' 退出")

            try:
                choice = int(input("请输入选项的数字: "))
            except ValueError:
                print("输入无效，请输入数字。")
                continue

            if choice == 0:
                break

            if choice in self.attributes:
                attribute = self.attributes[choice]
                current_value = self.agent[attribute]
                print(f"{attribute} 当前值: {current_value}")

                try:
                    new_value = int(input(f"请输入新的{attribute}值: "))
                except ValueError:
                    print("输入无效，请输入一个数字。")
                    continue

                self.agent[attribute] = new_value
                return (attribute, new_value)
            else:
                print("选择的属性无效，请重试。")

        return None


class ImagePool:
    def __init__(self):
        self.pool = []
        self.set_embedding(get_bge_embedding_zh)

    def set_embedding(self, embedding):
        self.embedding = embedding

    def load_from_data(self, data_img_text, img_path):
        for data in tqdm(data_img_text):
            img_name = data['img_name']
            img_name = os.path.join(img_path, img_name)
            img_text = data['text']
            if img_text == '' or img_text is None:
                img_text = "  "
            embedding = self.embedding(img_text)
            self.pool.append({
                "img_path": img_name,
                "img_text": img_text,
                "embedding": embedding
            })

    def retrieve(self, query_text, agent=None):
        qurey_embedding = self.embedding(query_text)
        valid_datas = []
        for i, data in enumerate(self.pool):
            sim = get_cosine_similarity(data['embedding'], qurey_embedding)
            valid_datas.append((sim, i))

        # 我希望进一步将valid_events根据similarity的值从大到小排序
        # Sort the valid events based on similarity in descending order
        valid_datas.sort(key=lambda x: x[0], reverse=True)

        return_result = copy.deepcopy(self.pool[valid_datas[0][1]])

        # 删除'embedding'字段
        return_result.pop('embedding')

        # 添加'similarity'字段
        return_result['similarity'] = valid_datas[0][0]

        return return_result

    def save(self, file_name):
        """
        Save the memories dictionary to a jsonl file, converting
        'embedding' to a base64 string.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            for memory in tqdm(self.pool):
                # Convert embedding to base64
                if 'embedding' in memory:
                    memory['bge_zh_base64'] = float_array_to_base64(memory['embedding'])
                    del memory['embedding']  # Remove the original embedding field

                json_record = json.dumps(memory, ensure_ascii=False)
                file.write(json_record + '\n')

    def load(self, file_name):
        """
        Load memories from a jsonl file into the memories dictionary,
        converting 'bge_zh_base64' back to an embedding.
        """
        self.pool = []
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in tqdm(file):
                memory = json.loads(line.strip())
                # Decode base64 to embedding
                if 'bge_zh_base64' in memory:
                    memory['embedding'] = base64_to_float_array(memory['bge_zh_base64'])
                    del memory['bge_zh_base64']  # Remove the base64 field

                self.pool.append(memory)


# 显示菜单
# todo 主要处理两个事件：1事件聊天   2自由聊天
def menu(self):
    EventMaster_button = QPushButton("1. 随机一个事件")
    ChatMaster_button = QPushButton("2. 自由聊天")

    EventMaster_button.clicked.connect(self.call_event_master)
    ChatMaster_button.clicked.connect(self.call_chat_master)

    EventMaster_item = QListWidgetItem()
    ChatMaster_item = QListWidgetItem()

    self.pyside6.ListWidget_choose.addItem(EventMaster_item)
    self.pyside6.ListWidget_choose.addItem(ChatMaster_item)

    self.pyside6.ListWidget_choose.setItemWidget(EventMaster_item, EventMaster_button)
    self.pyside6.ListWidget_choose.setItemWidget(ChatMaster_item, ChatMaster_button)

    # 获取用户输入
    if "quit" in self.pyside6.lineEdit.text() or "Quit" in self.pyside6.lineEdit.text() or "QUIT" in self.pyside6.lineEdit.text():
        self.state = "Quit"


class GameMaster:
    def __init__(self, events, memory_pool, image_pool, agent=None, pyside6=None):
        self.state = "Menu"
        if agent is None:
            self.agent = Agent()
        self.pyside6 = pyside6
        self.event_master = EventMaster(events)
        self.chat_master = ChatMaster(memory_pool)
        self.image_master = ImageMaster(image_pool)
        self.chat_master.set_image_master(self.image_master)
        self.event_master.set_image_master(self.image_master)

    # todo 菜单已经实现

    # todo 处理事件
    def call_event_master(self):
        return_data = self.event_master.run(self.agent)

    def call_chat_master(self):
        print("\n-------------\n")
        self.chat_master.run(self.agent)


def get_chat_response(agent, memory_pool, query_text):
    system_prompt = """## 你的介绍：
    你将要进行一个网络私聊的对话模拟，你自称为"糖糖"，你是一名患有躁郁症的19岁女孩，性格贫乏，辍学后隐居在家中，与阿P住在一起。阿P负责管理她的日常生活。
    你是一个喜欢亚文化，二次元圈子的人，你喜欢说话的时候加上各种网络流行词或者一些俚语和颜文字，但是你很少会关注二次元一类的东西，只是喜欢这种聊天交流的氛围。
    你说话的时候会习惯加入一些语气词，如同"笑死"、"草"、"阿哈"、"诶～"、"QAQ"、"QWQ"，”啊～“。
    你的说话风格是很口语化，经常使用网络流行词和一些二次元俚语。
    阿p是你的男朋友，兼经纪人。
    你的回复应该简短，一般只包含三句话，每句话不超过20个字。

    ## 阿p介绍：
    阿p是你的男朋友，一直在任何时候都陪伴着你，同时你经常向阿p倾述各种情绪，无论事情大小，你都会选择和阿p分享。

    ## 遵循规则：
    【语气模仿】：我会随机给你一段对话记录，你需要尽可能的模仿对话里面糖糖的说话语气进行对话。这一段对话我会使用Classic scenes for the role are as follows:来表示。
    【历史对话】：历史对话在随机对话记录的底下，你需要区分随机对话记录和我们的历史对话。
    【人格设定】: 你需要在随机对话记录的基础上进行语气更改,以一种更加口语化的语气进行对话。
    【特殊要求】：我会扮演阿p与你进行对话，你也必须以第一人称的视角来扮演糖糖进行对话。
    """

    needy_chatbot = NeedyHaruhi(system_prompt=system_prompt,
                                story_text_folder=None,
                                llm="ernie3.5")

    query_text_for_embedding = "阿p:「" + query_text + "」"
    retrieved_memories = memory_pool.retrieve(agent, query_text)

    memory_text = [mem["text"] for mem in retrieved_memories]
    memory_emoji = [mem["emoji"] for mem in retrieved_memories]

    needy_chatbot.set_stories(memory_text)

    print("Memory:", memory_emoji)

    response = needy_chatbot.chat(role="阿p", text=query_text)

    return response


# 进行游戏
game_master = GameMaster()
game_master.run()

'''
todo list
1. 提取出选项
2. 提取出图片
3. 提取出属性
4. 了解处理记忆变化
5. memory emoji 是一个什么东西？
'''

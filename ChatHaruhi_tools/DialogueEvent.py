import json
from ChatHaruhi_tools.util import parse_attribute_string
from ChatHaruhi_tools.util import parsing_condition_string


# 我希望实现一个python函数

# 分析一个字符串中有没有":"

# 如果有，我希望在第一个":"的位置分开成str_left和str_right，并以f"{str_left}:「{str_right}」"的形式输出

# 例子输入
# 爸爸:我真棒 
# 例子输出
# 爸爸:「我真棒」
# 例子输入
# 这一句没有冒号
# 例子输出
# :「这一句没有冒号」

def wrap_text_with_colon(text):
    # 查找冒号在字符串中的位置
    colon_index = text.find(":")

    # 如果找到了冒号
    if colon_index != -1:
        # 分割字符串为左右两部分
        str_left = text[:colon_index]
        str_right = text[colon_index + 1:]
        # 构造新的格式化字符串
        result = f"{str_left}:「{str_right}」"
    else:
        # 如果没有找到冒号，整个字符串被认为是右侧部分
        result = f":「{text}」"

    return result


# 给定 example_json_str = """{"prefix": "糖糖: 嘿嘿，最近我在想要不要改变直播风格，你觉得我应该怎么做呀？", "options": [{"user": "你可以试试唱歌直播呀！", "reply": "糖糖: 哇！唱歌直播是个好主意！我可以把我的可爱音色展现给大家听听！谢谢你的建议！", "attribute_change": "Stress: -1.0"}, {"user": "你可以尝试做一些搞笑的小品，逗大家开心。", "reply": "糖糖: 哈哈哈，小品确实挺有趣的！我可以挑战一些搞笑角色，给大家带来欢乐！谢谢你的建议！", "attribute_change": "Stress: -1.0"}, {"user": "你可以尝试做游戏直播，和观众一起玩游戏。", "reply": "糖糖: 游戏直播也不错！我可以和观众一起玩游戏，互动更加有趣！谢谢你的建议！", "attribute_change": "Stress: -1.0"}]}"""

# 我希望建立一个DialogueEvent类

# 这个类可以凭空初始化

# 也可以通过DialogueEvent(str)的方式来初始化

# 并且json_str解析后，会以self.data的字典形式存储在类中

# 并且可以通过类似 event["options"]的方式进行调用

# 请用python为我实现


class DialogueEvent:
    def __init__(self, json_str=None, user_role=None):
        if json_str:
            try:
                self.data = json.loads(json_str)
            except json.JSONDecodeError:
                print("输入的字符串不是有效的JSON格式。")
                self.data = {}
        else:
            self.data = {}

        if "condition" not in self.data:
            if "category" in self.data:
                self.data["condition"] = parsing_condition_string(self.data["category"])
            else:
                self.data["condition"] = None

        if "name" not in self.data:
            if "id" in self.data:
                self.data["name"] = self.data["id"]
            else:
                self.data["name"] = ""

        if "prefix_emoji" not in self.data:
            self.data["prefix_emoji"] = "📄"

        if "prefix" in self.data:
            self.data["prefix"] = self.data["prefix"].replace("：", ":")

        for option in self.data["options"]:
            if "user" in option:
                option["user"] = option["user"].strip(" ：")
            if "reply" in option:
                option["reply"] = option["reply"].replace("：", ":")
            if "option_emoji" not in option:
                option["option_emoji"] = "📄"

        if user_role is None:
            self.user_role = "阿P"

    def __getitem__(self, key):
        return self.data.get(key, None)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return str(self.data)

    def get_most_neutral(self):
        options = self.data["options"]

        if len(options) == 0:
            print('warning! no options can be selected')
            return 0

        i = 0
        min_change = 99999

        for i, option in enumerate(options):
            attr_change = parse_attribute_string(option["attribute_change"])
            current_change = 0
            for k in attr_change:
                current_change += abs(attr_change[k])

            if current_change < min_change:
                min_change = current_change
                choice_id = i

        return choice_id

    def get_emoji(self, choice_id):
        return self.data["prefix_emoji"] + self.data["options"][choice_id]["option_emoji"]

    def transfer_output(self, choice_id):
        line = wrap_text_with_colon(self.data["prefix"]) + "\n"
        if line.strip()[0] != "糖":
            line = "糖糖:" + line
        ans = line

        user_text = self.user_role + ":「" + self.data["options"][choice_id]["user"] + "」\n"
        ans += user_text
        line = wrap_text_with_colon(self.data["options"][choice_id]["reply"]) + "\n"
        if line.strip()[0] != "糖":
            line = "糖糖:" + line
        ans += line

        # print(self.data["options"][choice_id]['attribute_change'])
        return ans

    def most_neutral_output(self):
        neutral_id = self.get_most_neutral()
        return self.transfer_output(neutral_id), self.get_emoji(neutral_id)

    def get_text_and_emoji(self, choice_id):
        return self.transfer_output(choice_id), self.get_emoji(choice_id)


if __name__ == "__main__":
    example_json_str = """{"prefix": "糖糖: 嘿嘿，最近我在想要不要改变直播风格，你觉得我应该怎么做呀？", "options": [{"user": "你可以试试唱歌直播呀！", "reply": "糖糖: 哇！唱歌直播是个好主意！我可以把我的可爱音色展现给大家听听！谢谢你的建议！", "attribute_change": "Stress: -1.0"}, {"user": "你可以尝试做一些搞笑的小品，逗大家开心。", "reply": "糖糖: 哈哈哈，小品确实挺有趣的！我可以挑战一些搞笑角色，给大家带来欢乐！谢谢你的建议！", "attribute_change": "Stress: -1.0"}, {"user": "你可以尝试做游戏直播，和观众一起玩游戏。", "reply": "糖糖: 游戏直播也不错！我可以和观众一起玩游戏，互动更加有趣！谢谢你的建议！", "attribute_change": "Stress: -1.0"}]}"""

    # 通过给定的json字符串初始化DialogueEvent实例
    event = DialogueEvent(example_json_str)

    # 通过类似字典的方式访问数据
    # print(event["options"])  # 打印options字段的内容

    print(event.transfer_output(1))

    print(event.get_most_neutral())

    print(event.most_neutral_output())

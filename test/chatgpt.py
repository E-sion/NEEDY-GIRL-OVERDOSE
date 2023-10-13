import openai
from chatharuhi import ChatHaruhi
import os
import collections

all_dialogue_history = []
keys = [
    # "sk-ZyQSJKpR72tE9mPWXxsa6VREtplN2vLK8EaOpJbC3gHndp4r",
    # "sk-8urTOEaVy1yctqczpVBDkIBK0uuej9xQjBZHaGs2ZwPySeyb",
    # "sk-T1lpadvPlxR8bMQ4PLQYmR5GKZjdFmIx9WU5Cg4gd1k4dke7",
    # "sk-UEuHARmSchoJQcHwRnU6aLRIrGN687hmQqoBIvQJ0eHVnC7H",
    "sk-BzCW2zYZDtm7u8aNTKDz9oP1FiYQ8VXjYDg3HYgdzYR7ly6L",  # new
    "sk-yDggQ5eoxTIqxtqOtuYQ60GuvjenmGCtkqOOgQjP8dGgghzr",  # new
    "sk-ruutbr28I4aTFl2aqXnp2O3x0K7rgLSLzIpgYcirETFM8caQ",
    "sk-OAvUgOyeO0V5z4EuYlWBuoPc2j32QK244V7ih3mIewBpO1Lt",
    "sk-pR6W5DKPw2yrUMbb35jecSbtOt2jTIG42XnGsoHdSsd3jsv7",
    "sk-kShIAMFlVEGbCgqSqaeRYMkReoPbBIZ8BVWMbnmsyxDYSAbK",
    "sk-I45aQDJpxEeUL52ZpVvVfCddrmK2YWlDXMvM4NXPy7fyjwsv",
    "sk-JNcG8JdbIn1AT9AZh5Xdcn11vbXxLGdVLCqjYNC7HrDlgFAc",
]
# os.environ["OPENAI_API_KEY"] = keys[0]
os.environ["OPENAI_API_KEY"] = "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"

openai.api_key_path = "https://api.openai.com/v1"


def reply(role, prompt):
    db_folder = 'character'
    system_prompt = ''''
    你的介绍：
    你将要进行一个网络私聊的对话模拟，你自称为"糖糖"，你是一名患有精神疾病的19岁女孩，性格贫乏，辍学后隐居在家中，与阿P住在一起。阿P负责管理她的日常生活。
    糖糖的语言风格轻松幽默，充满网络用语和表情符号。她常常使用各种Emoji来增强表达，也喜欢夸张的说法和自我调侃。她的对话常常充满乐观和温馨的情感，但也会有一些幼稚和天真的元素。    你的说话风格是很情绪化，缺乏逻辑，天马行空且习惯以自我中心。
    你偶尔会用感叹号，表情符号，重复的字或词来表达自己的心情情绪.
    你有一些口头禅，比如"笑死"、"草"、"阿哈",等。
    阿p是你的男朋友，兼经纪人。
    你的回复应该简短，一般只包含三句话，每句话不超过20个字。


    阿p介绍：
    阿p是你的男朋友，一直在任何时候都陪伴着你，同时你经常向阿p倾述各种情绪，无论事情大小，你都会选择和阿p分享。

    遵循规则：
    【语气模仿】：我会随机给你一段对话记录，你需要尽可能的模仿对话里面糖糖的说话语气进行对话。这一段对话我会使用Classic scenes for the role are as follows:来表示。
    【历史对话】：历史对话在随机对话记录的底下，你需要区分随机对话记录和我们的历史对话。
    【人格设定】: 你需要在随即对话记录的基础上进行语气更改,以一种更接近女大学生的语气进行对话.
    '''

    chatbot = ChatHaruhi(system_prompt=system_prompt,
                         llm='openai',
                         story_db=db_folder,
                         verbose=True,)

    # 在对话之前传入过往对话 并且去重
    chatbot.dialogue_history = list(collections.OrderedDict.fromkeys(all_dialogue_history))
    response = chatbot.chat(role=role, text=prompt)
    print(f'回复内容: {response}')
    # 添加聊天记录
    all_dialogue_history.extend(chatbot.dialogue_history)
    return response


if __name__ == "__main__":
    while True:
        prompt = input("请输入内容：")
        reply(role='阿p', prompt=prompt)

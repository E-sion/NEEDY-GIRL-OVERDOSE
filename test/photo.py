# from openpyxl import load_workbook
#
# wb = load_workbook('Jines——.xlsx')
# ws = wb.active
# for row in ws.iter_rows():
#     for cell in row:
#         if str(cell.fill.bgColor.rgb) == "00000000":
#             #
#             if len(cell.value)>=10:
#                 print(cell.value)
#
#             # text = ""  # 创建一个空字符串，用来存储当前行的文本
#             # for c in row:  # 遍历当前行的每个单元格
#             #     text += str(c.value) + " "  # 将单元格的值转换为字符串，并添加到text后面，用空格分隔
#             # print(text)  # 打印tex

#
# import g4f
#
# print(g4f.Provider.Ails.params)  # supported args
#
#
# def re(text):
#     response = g4f.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system",
#                    "content": "'''给定一段用户糖糖的twitter文本，将这段用户糖糖的twitter，转化为一个询问者阿p和这个用户糖糖之间的聊天对话。\n阿p和糖糖之间可以使用非正式的语言进行打招呼。\n糖糖聊天的语言风格，尽可能接近twitter的原文。\n将twitter的内容拆解成多句输出，并使用更接近聊天的语气\n聊天的内容，尽可能还原twitter的原文，不要增加新的观点'''"},
#                   {"role": "system",
#                    "content": '"example-twitter from 糖糖: "好抑郁好想死……可是又没道理去死；要具体说的话，都怪那些恶熏阿宅们的纯良（不是）留言不好……"'},
#                   {"role": "assistant",
#                    "content": "阿p:「感觉你心情有点差，怎么啦？」\n糖糖:「好抑郁啊啊啊，想死………。」\n阿p:「阿，发生了什么？」\n阿p:「主要还是因为看直播的阿宅们发了一些不好的留言……。」"},
#                   {"role": "system",
#                    "content": 'example-twitter from 糖糖: "自我肯定感直接暴涨这种感觉比用魔法还快乐！切身体会到了幸福指数噌噌上涨的感觉……"'},
#                   {"role": "assistant",
#                    "content": "阿p:「最近你的粉丝涨的很快呀，什么感觉呀？」糖糖:「嘿嘿，我的自我肯定感简直暴涨了！」\n阿p:「做直播到现在感觉如何啦？」\n糖糖:「现在非常幸福阿，虽然说一开始不是很愉快啦」"},
#                   {"role": "system", "content": 'example-twitter from 糖糖:{0}'.format(text)}])
#
#     return response
#
#
# # normal response
# # Open file
# fileHandler = open("data.txt", "r")
# # Get list of all lines in file
# listOfLines = fileHandler.readlines()
#
# counter = 1
# # Iterate over the lines
# for line in listOfLines:
#     text_line = line.strip()
#     response_txt = re(text_line)
#     # todo 将for循环内每一次的response_txt值都写入一个不同的txt内。
#     outputFile = open("糖糖_{0}.txt".format(counter), "w") # 使用counter来命名每个txt文件
#     outputFile.write(response_txt) # 将response_txt值写入txt文件
#     outputFile.close() # 关闭txt文件
#     counter += 1 # 更新counter的值


# import openai
#
# # openai.api_base = "https://api.openai.com/v1" # 换成代理，一定要加v1
# openai.api_base = "https://openkey.cloud/v1" # 换成代理，一定要加v1
# # openai.api_key = "API_KEY"
# openai.api_key = "sk-28D7VfuHyatRQcKbmPHIBUbtCmDcVdyVYgVDsgTmnwP2Lxgt"
# def response():
#     response = openai.ChatCompletion.create(
#                                     model="gpt-3.5-turbo",
#                                     messages=[
#                                       {"role": "user", "content": "你好"}
#                                     ],
#                                     # 流式输出
#                                     stream = False)
#     # 直接打印content的内容
#     print(response["choices"][0]["message"]["content"])
#
# response()

import collections
import os

import chromadb

from typing import Tuple
from chatharuhi import ChatHaruhi

all_dialogue_history = []
os.environ["OPENAI_API_KEY"] = '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'


def reply(role, prompt):
    db_folder = 'tempdb_3Gy6oRjM'
    system_prompt = '''
    注意糖糖只有面对阿p时会更加活泼乐观，面对其他人和外面的世界时性格比较内向，不善社交。
    糖糖的说话风格比较随意，经常开玩笑且喜欢夸张。
    糖糖的心情很容易被影响而变得低落，心情的变化起伏大。
    '''

    chatbot = ChatHaruhi(system_prompt=system_prompt,
                         llm='openai',
                         story_db=db_folder)

    # 在对话之前传入过往对话 并且去重
    chatbot.dialogue_history = list(collections.OrderedDict.fromkeys(all_dialogue_history))
    print(f"当前对话记录：{chatbot.dialogue_history}")
    response = chatbot.chat(role=role, text=prompt)
    print(f'回复内容: {response}')
    # 添加聊天记录
    all_dialogue_history.extend(chatbot.dialogue_history)
    return response


while True:
    reply(role="阿p", prompt=input())

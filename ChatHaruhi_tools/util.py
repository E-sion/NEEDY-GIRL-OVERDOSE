import re


# 我希望实现一个字符串解析函数，输入是一个string，输出是一个dict，如果字符串中出现
# "Strees:", "Affection:"或者"Darkness:"，则把后面的一个有正负的浮点数作为value，对应的字符串作为key，记录在dict中

# 如果后面是？或者非数字，则记录成0

# example input:
# Stress: -1.0, Affection: +0.5
# example output:
# {"Stress":-1,"Affection":0.5 }

# exmple input:
# Affection: +4.0, Stress: -2.0, Darkness: -1.0
# example output:
# {"Stress":-1,"Affection":0.5 }

# example input:
# Affection: +2.0, Stress: -1.0, Darkness: ?
# example output:
# {"Affection": 2, "Stress": -1, "Darkness": 0 }

# example input:
# Stress: -1.0
# example output:
# {"Stress":-1}

def parse_attribute_string(attribute_str):
    result = {}
    patterns = {
        "Stress": r"Stress:\s*([+-]?\d+(\.\d+)?)?",
        "Affection": r"Affection:\s*([+-]?\d+(\.\d+)?)?",
        "Darkness": r"Darkness:\s*([+-]?\d+(\.\d+)?)?"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, attribute_str)
        if match:
            value = match.group(1)
            if value is None:
                result[key] = 0
            else:
                result[key] = float(value)

    return result

# 我希望实现一个字符串解析函数，输入是一个string，输出是一个tuple，

# max_value = 100，字符串中可能会包含Darkness，Stress或者Affection属性中的一种，

# 如果输入为"Affection 61+", 则输出 ("Affection", 61, 100)

# 如果输入为"Darkness 0-39"，则输出 ("Darkness", 0, 39)

# 输出字符串中包含的属性，区间的最小值和最大值。

# 如果不包含任何属性，则输出None

# example_input:
# Random Noon Event: Darkness 0-39
# example_output
# ("Darkness", 0 , 39)

# example_input:
# Random Noon Event: Stress 0-19
# example_output
# ("Stress", 0 , 19)

# example_input:
# Random Noon Event: Affection 61+
# example_output
# ("Affection", 61, 100)

import re

def parsing_condition_string(s):
    max_value = 100  # 定义最大值
    # 正则表达式匹配'属性 最小值-最大值'或'属性 最小值+'
    pattern = re.compile(r'(Darkness|Stress|Affection)\s+(\d+)(?:-(\d+)|\+)')

    match = pattern.search(s)
    if match:
        attribute = match.group(1)  # 属性
        min_value = int(match.group(2))  # 最小值
        # 如果有最大值就直接使用，没有就用默认的max_value
        max_value = int(match.group(3)) if match.group(3) else max_value
        return (attribute, min_value, max_value)
    
    return None  # 如果没有匹配则返回None


#------ BGE Embedding -----------

from transformers import AutoModel, AutoTokenizer
import torch

_bge_model_zh = None
_bge_tokenizer_zh = None

def get_bge_embeddings_zh( sentences ):
    # unsafe ensure batch size by yourself

    global _bge_model_zh
    global _bge_tokenizer_zh

    if _bge_model_zh is None:
        from transformers import AutoTokenizer, AutoModel
        _bge_tokenizer_zh = AutoTokenizer.from_pretrained('BAAI/bge-small-zh-v1.5')
        _bge_model_zh = AutoModel.from_pretrained('BAAI/bge-small-zh-v1.5')

    _bge_model_zh.eval()

    # Tokenize sentences
    encoded_input = _bge_tokenizer_zh(sentences, padding=True, truncation=True, return_tensors='pt', max_length = 512)

    # Compute token embeddings
    with torch.no_grad():
        model_output = _bge_model_zh(**encoded_input)
        # Perform pooling. In this case, cls pooling.
        sentence_embeddings = model_output[0][:, 0]
    # normalize embeddings
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    return sentence_embeddings.cpu().tolist()

def get_bge_embedding_zh( text_or_texts ):
    if isinstance(text_or_texts, str):
        return get_bge_embeddings_zh([text_or_texts])[0]
    else:
        return get_bge_embeddings_zh(text_or_texts)


# Encode和Decode的代码来自于ChatHaruhi

import base64
import struct

def float_array_to_base64(float_arr):
    
    byte_array = b''
    
    for f in float_arr:
        # 将每个浮点数打包为4字节
        num_bytes = struct.pack('!f', f)  
        byte_array += num_bytes
    
    # 将字节数组进行base64编码    
    base64_data = base64.b64encode(byte_array)
    
    return base64_data.decode('utf-8')

def base64_to_float_array(base64_data):

    byte_array = base64.b64decode(base64_data)
    
    float_array = []
    
    # 每 4 个字节解析为一个浮点数
    for i in range(0, len(byte_array), 4):
        num = struct.unpack('!f', byte_array[i:i+4])[0] 
        float_array.append(num)

    return float_array

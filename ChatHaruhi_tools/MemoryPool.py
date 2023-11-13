from tqdm import tqdm

from ChatHaruhi_tools.util import float_array_to_base64, base64_to_float_array
from ChatHaruhi_tools.util import get_bge_embedding_zh
import json
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# compute cosine similarity between two vector
def get_cosine_similarity( v1, v2):
    v1 = torch.tensor(v1).to(device)
    v2 = torch.tensor(v2).to(device)
    return torch.cosine_similarity(v1, v2, dim=0).item()


class MemoryPool:
    def __init__(self):
        self.memories = {}
        self.diff_threshold = 20
        self.top_k = 7
        self.set_embedding( get_bge_embedding_zh )

    def set_embedding( self, embedding ):
        self.embedding = embedding

    def load_from_events( self, events ):
        for event in tqdm( events ):

            if len(event["options"])>0:
                text, emoji = event.most_neutral_output()
            else:
                text = event["prefix"]
                emoji = event["prefix_emoji"]
                
            embedding = self.embedding( text )

            condition = event["condition"]
            if condition is None:
                memory_attribute = ("Stress", 10 )
            else:
                memory_attribute = (condition[0],(condition[1]+ condition[2])//2 )

            name = event["name"]

            memory = {
                "name": name,
                "text": text,
                "embedding": embedding,
                "memory_attribute": memory_attribute,
                "emoji": emoji # TODO
            }

            self.memories[ name ] = memory

# 我希望为这个类进一步实现save和load函数，save函数可以将memories中的每一个value对应的dict，存储到一个jsonl中，load函数可以读取回来。注意编码都要使用utf-8, ensure_ascii = False

# 我希望修改save和load函数

# 其中memory中会有embedding字段

# from util import float_array_to_base64
# from util import base64_to_float_array

# 我希望在save的时候，把embedding字段用float_array_to_base64替换为base64字符串，并且字段改名为bge_zh_base64

# 在load的时候再把bge_zh_base64字段用base64_to_float_array，解码为embedding

    def save(self, file_name):
        """
        Save the memories dictionary to a jsonl file, converting
        'embedding' to a base64 string.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            for memory in tqdm(self.memories.values()):
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
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in tqdm(file):
                memory = json.loads(line.strip())
                # Decode base64 to embedding
                if 'bge_zh_base64' in memory:
                    memory['embedding'] = base64_to_float_array(memory['bge_zh_base64'])
                    del memory['bge_zh_base64']  # Remove the base64 field
                
                self.memories[memory['name']] = memory


    def change_memory( self, memory_name , new_text , new_emoji = None):
        if memory_name in self.memories:
            memory = self.memories[memory_name]
            memory["text"] = new_text
            memory["embedding"] = self.embedding( new_text )
            if new_emoji:
                memory["emoji"] = new_emoji

    def retrieve( self, agent, query_text ):
        query_embedding = self.embedding( query_text )

        valid_events = []

        # filter valid memory
        for key in self.memories:
            memory = self.memories[key]
            attribute, value = memory["memory_attribute"]
            if abs(agent[attribute] - value) <= self.diff_threshold:
                # valid memory
                simlarity = get_cosine_similarity(query_embedding, memory["embedding"])
                valid_events.append((simlarity, key) )

        # 我希望进一步将valid_events根据similarity的值从大到小排序
        # Sort the valid events based on similarity in descending order
        valid_events.sort(key=lambda x: x[0], reverse=True)

        result = []

        for _,key in valid_events:
            result.append(self.memories[key])
            if len(result)>=self.top_k:
                break
        return result
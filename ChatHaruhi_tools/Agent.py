# Implemented by 李鲁鲁
#
# ChatHaruhi_tools X 主播女孩重度依赖，
#
# 母项目主页 https://github.com/LC1332/Chat-Haruhi-Suzumiya
#
# 我希望实现一个Agent类
#
# 这个agent有多个属性（目前设计有 Stress , Darkness和Affection）
#
# 可以通过类似agent["Stress"]这样的形式调用
#
# 请用self.attributes 字典形式存储，并且重载[]操作符使得agent的行为和字典一致
#
# 同时实现一个成员函数apply_attribute_change( attribute_change )
#
# attribute_change是一个形如{"Darkness":-1, "Stress":1}的字典，如果字典key的值在self.attributes中存在，则累加在上面，不然则汇报warning并跳过

import json


class Agent:

    def __init__(self, attributes_str=None):
        if attributes_str:
            attributes = json.loads(attributes_str)
        else:
            attributes = {
                "Stress": 0,
                "Darkness": 0,
                "Affection": 0
            }
        self.attributes = attributes

    def save_to_str(self):
        return json.dumps(self.attributes, ensure_ascii=False)

    def __getitem__(self, key):
        return self.attributes.get(key)

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def apply_attribute_change(self, attribute_change):
        for key, value in attribute_change.items():
            if key in self.attributes:
                self.attributes[key] += value
                if self.attributes[key] < 0:
                    self.attributes[key] = 0
            else:
                print(f"Warning: {key} not in attributes, skipping")

    def in_condition(self, condition):
        if condition is None:
            return True
        if condition[0] in self.attributes:
            return self.attributes[condition[0]] >= condition[1] and self.attributes[condition[0]] <= condition[2]
        else:
            return False


if __name__ == "__main__":
    # 示例用法
    agent = Agent()
    print(agent["Stress"])  # 输出 0
    agent["Stress"] += 1
    print(agent["Stress"])  # 输出 1
    agent.apply_attribute_change({"Darkness": -1, "Stress": 1})
    print(agent["Darkness"])  # 输出 -1
    print(agent["Stress"])  # 输出 2
    agent.apply_attribute_change({"Nonexistent": 5})  # 输出 Warning: Nonexistent not in attributes, skipping

    condition = ('Stress', 0, 19)

    print(agent.in_condition(condition))

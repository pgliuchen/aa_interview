"""
实现一个函数：
输入是两个字典，要求从第二个字典中删除所有key是第一个字典的value的记录，并返回结果
例如：dict_1 = {"a": "bbb"} dict_2={"bbb": "c", "a": "ccc"}
经过 operate_two_dicts(dict_1, dict_2) 处理之后
返回 {"a": "ccc"}
"bbb"被删掉了
"""


def operate_two_dicts(dict_1, dict_2):
    raise NotImplementedError()


if __name__ == '__main__':
    print(operate_two_dicts({"a": "bbb"}, {"bbb": "c", "a": "ccc"}))

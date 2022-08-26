# -*-coding:utf-8-*-


import json


user = {'name': 'Jack', 'age': 30}
print(type(user))

json_str = json.dumps(user)
print(type(json_str))

# 写入文件
with open('json.json', 'w') as f:
    json.dump(user, f)

# 读取文件
with open('json.json') as f:
    json_dict = json.load(f)
    print(type(json_dict))
    print(json_dict)

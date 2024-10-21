import json

my_list = [{"name": "liYong", "age": 23}, {"name": "zhangSan", "age": 24}, {"name": "wangWu", "age": 22}]
# listTOjson
json_str = json.dumps(my_list)
print(type(json_str))
print(json_str)

my_str = '[{"name":"liYong","age":23},{"name":"zhangSan","age":24},{"name":"wangWu","age":22}]'
# json To list or dict
ls = json.loads(my_str)
print(type(ls))
print(ls)

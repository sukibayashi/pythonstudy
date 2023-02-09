dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 1. [key]
# print(dict1['name']) # 返回對應的值(key 存在)
# print(dict1['id'])

# 2. 函數
# 2.1 get()
# print(dict1.get('name'))
# print(dict1.get('names')) # 如果 key 不存在，返回None
# print(dict1.get('names', '無'))

# 2.2 keys() 查找字典中所有的 key， 返回可迭代對象
# print(dict1.keys())

# 2.3 values() 查找字典中的所有 value，返回可迭代對象
# print(dict1.values())

# 2.4 items() 查找字典中所有的鍵值對，返回可迭代對象，裡面的數據是元祖，元祖數據1是字典的key，元祖數據2是字典key對應的值
print(dict1.items())
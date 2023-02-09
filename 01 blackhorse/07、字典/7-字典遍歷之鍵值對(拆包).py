dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# xx.items() 返回可迭代對象，內部是元祖，元祖有2個數據
# 元祖數據1是字典的key，元祖數據2是字典的value
for key,value in dict1.items():
	# print(key)
	# print(value)
	# 目標： key = value
	print(f'{key} = {value}')
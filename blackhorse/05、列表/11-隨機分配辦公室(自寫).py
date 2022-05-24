# 需求：8位老師，3個辦公室，將8位老師隨機分配到辦公室

"""
步驟
1. 準備數據
    1.1 8位老師 -- 列表
    1.2 3個辦公室 -- 列表嵌套
2. 分配老師到辦公室
    *** 隨機分配
    把老師的名字寫入到辦公室列表 -- 辦公室列表追加老師名字數據
3. 驗證是否分配成功
    打印辦公室詳細信息：每個辦公室的人數和對應老師的名字
"""
# 1. 準備數據
name_list = ['小紅', '小明', '小張', '小王', '小雪', '小周', '小吳', '小楊']
class_list = [[], [], []]

# 2. 分配老師到辦公室 -- 取到每個老師放到辦公室列表 -- 遍歷老師列表數據
# y = 0
# for i in name_list:
#     if y == 3:
#         y = 0
#         class_list[y].append(i)
#     else:
#         class_list[y].append(i)
#         y += 1
# print(class_list)

import random
for name in name_list:
    a = random.randint(0, len(class_list)-1)
    class_list[a].append(name)
print(class_list)



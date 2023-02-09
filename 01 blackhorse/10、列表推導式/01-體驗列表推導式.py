# 需求：0，1，2，4..
# 1. 循環實現； 2. 列表推導式（化簡代碼：創建或控制有規律的列表）
'''
1.1 創建空列表
1.2 循環將有規律的數據寫入到列表
'''

# while實現---------------
# list1 = []
#
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
# print(list1)

# for 實現-----------------
# list1 = []
# for i in range(10):
#     list1.append(i)
# print(list1)

# 列表推導式----------------
list1 = [i for i in range(10)]
print(list1)
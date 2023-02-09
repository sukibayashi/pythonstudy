list1 = ['a', 'b', 'c', 'd', 'e']

# enumerate 返回結果是元祖，元祖第一個數據是原迭代對象的數據對應的下標，元祖第二個數據是原迭代對象的數據
# for i in enumerate(list1):
#     print(i)

# for i in enumerate(list1, start=1):
#     print(i)

for index, char in enumerate(list1, start=1):
    print(f'下標是{index}, 對應的字符是{char}')


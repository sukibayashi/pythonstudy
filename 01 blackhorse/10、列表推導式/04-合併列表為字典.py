# 當列表長度一致時
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

# 當列表長度不一致時
list3 = ['name', 'age', 'gender', 'id']
list4 = ['Tom', 20, 'man']

# 就會報錯
# dict2 = {list3[i]:list4[i] for i in range(len(list3))}
# 總結
# 1. 如果兩個列表數據個數相同，len 統計任何一個列表的長度都可以
# 2. 如果兩個列表數據個數不同，len 統計數據多的列表數據個數會報錯；len 統計數據少的列表數據就不會報錯

# 解決方法
dict2 = {list3[i]: list4[i] for i in range(min(len(list3), len(list4)))}  # 取最短的長度
print(dict2)

list1 = [10, 20, 30, 20, 40, 50]
s1 = {100, 300, 200, 500}
t1 = ('a', 'b', 'c', 'd', 'e')

# tuple(): 轉換成元祖
print(tuple(list1))
print(tuple(s1))

# list(): 轉換成列表
print(list(s1))
print(list(t1))

# set()：轉換成集合（重複的數據會合併）
print(set(list1))
print(set(s1))
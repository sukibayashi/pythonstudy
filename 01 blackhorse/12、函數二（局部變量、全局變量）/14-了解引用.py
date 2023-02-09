# 可變和不可變

# 1. 不可變: int:
# 1.1 聲明變量保存整型數據，把這個數據賦值到另一個變量： id（）檢測兩個變量的id值（內存的十進制值）
# a = 1
# b = a

# 發現a和b的值是相同的
# print(b)
# print(id(a))
# print(id(b))

# 修改a的數據測試id值
# a = 2
# print(b)

# 因為修改了a的數據，內存要開闢另外一份內存取存儲2，id檢測a和b的地址不同
# print(id(a))
# print(id(b))


# 2. 可變類型：列表
aa = [10, 20]
bb = aa
print(bb)

print(id(aa))
print(id(bb))

aa.append(30)
print(aa)
print(bb)  # 列表是可變類型，所以會修改值

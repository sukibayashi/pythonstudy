a = 10
b = 20

# 1. 方法一
"""
1.1 定義中間的第三變量，為了臨時存儲a或b的數據
1.2 把a的數據存儲到c，做保存
1.3 把b的數據複製到a, a = 20
1.4 把c的數據複製到b， b = 10
"""
c = 0
c = a
a = b
b = c

print(a)
print(b)

c, d = 1, 2
# c, d = d, c
c, d = d, c
print(c)
print(d)



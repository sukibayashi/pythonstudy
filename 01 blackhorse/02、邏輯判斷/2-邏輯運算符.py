a = 0
b = 1
c = 2

# 1. and: 與 都真才真
print(a < b and c > b)

# 2. or：或 一真則真，都假才假
print(a > b or b < c)
print(a < b or b > c)

# 3. not：非 取反(如果為True，則返回false。如果為false，則返回true)
print(not False)
print(not c > b)
print(not c < b)

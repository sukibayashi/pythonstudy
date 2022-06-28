# 1. 任意三個數之和
def sum_num(a, b, c):
    return a + b + c


# result = sum_num(1, 2, 3)
# print(result)


# 2. 任意三個數求平均值
def average_num(a, b, c):
    sumResult = sum_num(a, b, c)
    return sumResult / 3


result = average_num(1, 2, 3)
print(result)

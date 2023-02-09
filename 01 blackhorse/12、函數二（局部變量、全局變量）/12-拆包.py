# 1. 拆包元組數據:
def return_num():
    return 100, 200


# result = return_num()
# print(result)
# num1, num2 = return_num()
# print(num1)
# print(num2)


# 2. 字典數據拆包
# 先準備字典，然後拆包
dict1 = {'name': 'Tom', 'age': 20}
# dict1中有兩個鍵值對，拆包的時候用兩個變量接收數據
a, b = dict1
print(a)
print(b)

# v值
print(dict1[a])
print(dict1[b])

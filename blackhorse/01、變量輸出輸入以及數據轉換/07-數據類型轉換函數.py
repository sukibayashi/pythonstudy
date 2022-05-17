# 1. float() -- 將數轉換成浮點型
num1 = 1
str1 = '10'
print(type(float(num1))) # float
print(float(num1)) # 1.0
print(float(str1)) # 10.0

# 2. str() -- 將數據轉換成字符串形
print(type(str(num1))) # str

# 3. tuple() -- 將一個序列轉換成元祖
list1 = [10, 20, 30]
print(tuple(list1)) # tuple

# 4. list() -- 將一個序列轉換成列表
t1 = (100, 200, 300)
print(list(t1)) # list

# 5. eval() -- 計算字符串中的有效 Python 表達式，並返回一個對象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(eval(str2))
print(eval(str3))
print(eval(str4))
print(eval(str5))
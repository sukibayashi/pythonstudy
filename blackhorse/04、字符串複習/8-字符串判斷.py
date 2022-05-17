mystr = "   hello world and itcast and itheima and Python"
mystr2 = mystr.strip()

# 1. startswith()：判斷字符串是否以某個子串開頭
# print(mystr2.startswith('hello'))
# print(mystr2.startswith('world', 6))

# 2. endswitch()：判斷字符串是否以某個子串結尾
# print(mystr.endswith('Pythons'))

# 3. isalpha()：字母
#print(mystr2.isalpha())

# 4. isdigit()：數字
mystr3 = '123456你真聰明'
# print(mystr3.isdigit())

# 5. isalnum()：數字或字母或組合
print(mystr3.isalnum())

# 6. isspace()：空格
mystr5 = '1 2 3 4 5 6'
mystr5 = '     '
print(mystr5.isspace())
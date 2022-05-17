mystr = "hello world and itcast and itheima and Python"

# 1. replace()：把 and 換成 和
# 說明 replace 函數有返回值，返回值是修改後的字符串，但不會改變原本的字符串
# 調用了 replace 函數後，發現原有的字符串的函數並沒有做到修改，修改後的數據都是 replace 函數的返回值。
# 說明字符串是不可變數據類型。int,str,float...數據會分為兩大類：1.可變類型。 2. 不可變類型
# 不可變字符串要把修改的結果賦值到新的字符串上，原有的字符串不會發生任何的變動
# new_mystr = mystr.replace('and','和')

# 如果替換次數超過字符串所擁有的次數，則表示替換字符串中所有要替換的子串。
# new_mystr2 = mystr.replace('and','和', 10)
# print(new_mystr)
# print(new_mystr2)

# 2. split() -- 分隔，返回一個列表,丟失分隔字符
# list1 = mystr.split('and')
# list2 = mystr.split('and', 2)
# print(list1)
# print(list2)

# 3. join() -- 合併列表裡面的字符串數據為一個大字符串
mylist = ['aa', 'bb', 'cc']

# aa...bb...cc
new_str = '...'.join(mylist)
print(new_str)
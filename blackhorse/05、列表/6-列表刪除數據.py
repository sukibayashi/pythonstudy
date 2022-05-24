name_list = ['eric', 'sam', 'alice']

# 1. del
# del name_list

# del 可以刪除指定下標的數據
# del name_list[0]
# print(name_list)

# 2. pop()：刪除指定下標的數據，如果不指定下標，默認刪除最後一個數據，
# 無論是按照下標還是刪除最後一個，pop函數都會返回這個被刪除的數據。
# del_name = name_list.pop()
# print(del_name)

# 3. remove(數據)
# name_list.remove('eric')
# print(name_list)

# 4. clear() -- 清空
name_list.clear()
print(name_list)


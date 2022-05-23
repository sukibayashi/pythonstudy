name_list = ['eric', 'sam', 'alice']

# 需求：註冊郵箱，用戶輸入一個賬號名，判斷這個賬號是否存在。如果存在，提示用戶，否則提示可以註冊
name = input('請輸入你的用戶名：')

while name in name_list:
    # 提示用戶名已存在
    print(f'您輸入的用戶名 {name} 已被使用')
    name = input('請重新填寫一個用戶名：')
else:
    # 列表數據是可改的，列表是可變類型
    # append 函數追加數據的時候如果數據是一個序列，追加整個序列到列表的結尾。 .append([11,22])
    name_list.append(name)
    print(f'恭喜你，{name} 註冊成功！')
    print(name_list)
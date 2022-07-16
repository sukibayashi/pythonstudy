# 1. 显示功能界面

def info_print():
    print('请选择功能===========')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、显示所有学员信息')
    print('6、退出系统')
    print('=' * 19)


# 等待存儲所有學員的信息
# info = []


info = [{'id': '1', 'name': '潘', 'gender': '男'}, {'id': '2', 'name': '楊', 'gender': '女'}]


# 添加學員信息的函數
def add_info():
    """添加學員函數"""
    # 1. 用戶輸入，接受用戶輸入學員信息
    new_id = input('請輸入學號： ')
    new_name = input('請輸入姓名： ')
    new_gender = input('請輸入性別： ')

    # 聲明info是全局變量
    # 2. 判斷是否添加這個學員：如果學員姓名已經存在報錯提示；如果姓名不存在添加數據
    global info

    # 2.1 不允許姓名重複：判斷用戶輸入的姓名和列表裡面字典的name對應的值相等，提示(列表嵌套)
    for i in info:
        if new_name == i['name']:
            print('該用戶已經存在！')
            # return作用：退出當前函數，後面添加信息的代碼不執行
            return
    # 2.2 如果輸入的姓名不存在，添加數據，準備空字典，字典新增數據，列表追加字典
    info_dict = {}

    # 將用戶輸入的數據追加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['gender'] = new_gender

    # 將這個學員的字典數據追加到列表
    info.append(info_dict)
    info = sorted(info, key=lambda x: (x['id']))
    print(info)


# 查詢學生序號
def search_info():
    new_id = int(input('請問輸入學生學號？ ')) - 1
    print(info[new_id])


# 刪除學員
def del_info():
    """刪除學員"""
    # 1. 用戶輸入要刪除的學員的姓名
    print('===================')
    new_name = input('請輸入要刪除的學員的姓名： ')
    check_del = input(f'確認要刪除 {new_name} 的資料嗎？（yes/no) ')
    print('===================')

    # 如果確定刪除資料
    while check_del != 'yes':
        print('輸入錯誤，請重新輸入！')
        check_del = input(f'確認要刪除 {new_name} 的資料嗎？（yes/no) ')
    else:
        # 2. 判斷學員是否存在：存在則刪除；不存在提示
        # 2.1 聲明info是全局變量
        global info
        # 2.2 遍歷列表
        for i in info:
            # 2.3 判斷學員是否存在：存在執行刪除（列表裡面的字典），break： 這個系統不允許籌碼，刪除了一個後面不需要遍歷：不存在提示
            if new_name == i['name']:
                # 列表删除数据 -- 按数据删除remove
                info.remove(i)
                print('删除成功！')
                print(info)
                break
        else:
            print('该学员不存在')


# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3. 按照用户输入的功能序号，执行不同的功能（函数）
    # 如果用户输入1，执行添加； 如果用户输入2，执行删除...
    if user_num == 1:  # 添加
        print('添加')
        add_info()
    elif user_num == 2:  # 刪除
        del_info()
    elif user_num == 3:  # 修改
        print('修改')
    elif user_num == 4:  # 查找
        search_info()
    elif user_num == 5:
        print(info)
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('===================')
        print('輸入的功能有誤，請重新選擇功能')

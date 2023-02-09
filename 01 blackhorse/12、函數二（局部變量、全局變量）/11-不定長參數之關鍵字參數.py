# 收集所有關鍵字參數，返回一個字典
def user_info(**kwargs):
    print(kwargs)


user_info()
user_info(name='Tom')
user_info(name='Tom', age=18, id=110)
# 接收所有位置參數，返回一個元組
def user_info(*args):
    print(args)


user_info('Tom', 18)
user_info('Tom', 18, 'man')
user_info()

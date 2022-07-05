# 需求： 函數3個參數 name, age, gender
def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年齡是{age}, 性別是{gender}')


# user_info('Tom', 20, '男')
user_info(20, '男')  # 個數定義和傳入不一致會報錯
# user_info( 20,'Tom','男') # 順序也和定義必須是一致的，否則導致數據無意義。

def user_info(name, age, gender='男'):
    print(f'您的姓名是{name}, 年齡是{age}, 性別是{gender}')


user_info('Tom', 18)  # 沒有為缺省參數傳值，表示使用默認值
user_info('Tom', 18, gender='女')  # 為缺省參數傳值，使用這個值，即修改了默認值


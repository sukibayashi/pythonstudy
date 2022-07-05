def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年齡是{age}, 性別是{gender}')


# 調用函數傳參
user_info('Rose', age=20, gender='女')
user_info('小明', gender='男', age=18)  # 關鍵字參數之間不分先後順序

# 位置參數必須寫在關鍵字參數的前面
# user_info(age=18, '小明', gender='男')

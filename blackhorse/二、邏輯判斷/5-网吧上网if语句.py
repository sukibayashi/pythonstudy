"""
1. 用户输入
2. 保存用户输入的年龄
3. if
"""

age = eval(input('请输入你的年龄：\n'))
printage = str(input(f'你输入的年龄是{age}吗？ (yes/no) \n'))

while printage != ('yes'):
    age = eval(input('请输入你的年龄：\n'))
    printage = str(input(f'你输入的年龄是{age}吗？ (yes/no) \n'))
    continue
else:
    if age >= 18:
        print('恭喜你，已经成年，可以上网')
    else:
        print(f'才{age}岁？毛还没有长齐就想玩电脑？')





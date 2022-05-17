money = str(input('请输入你是否帶錢了： (yes/no)\n ' ))


if money == ('yes'):
    print('你能上車')

    seat = str(input('请输入你是否看到座位：(yes/no) \n '))

    if seat ==('yes'):
        print('趕緊坐下')
    else:
        print('請站著吧')
else:
    print('你不能上車')
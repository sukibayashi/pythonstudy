i = 1
while i <= 5:
    print('老婆，我錯了')
    i += 1
value1 = str(input('你原諒他了嗎？(yes/no) ' ))
while value1 != 'yes':
    print('你以為這就結束了？')
    i = 1
    while i <= 5:
        print('老婆，我錯了')
        i += 1
    value1 = str(input('你原諒他了嗎？(yes/no) '))
else:
    print('原諒你了')

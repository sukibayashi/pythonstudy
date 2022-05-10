count=0

# while count != 5:
while count < 5:
    count += 1
    print('老婆我錯了')


# print('老婆你錯了'*5)
answer = str(input('要原諒他嗎？ (yes/no)\n'))
if answer == 'yes':
    print('我原諒你了')
else:
    print('再好好想想吧')
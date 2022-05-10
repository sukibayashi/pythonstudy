# 如果吃的過程中，吃到第三個吃飽了，則不需要再吃第四個和第五個蘋果，即吃蘋果的動作停止，這裡就是break控制循環流程，即終止此循環。
'''
i = 1
while i <= 5:
    if i == 4:
        print('我吃飽了')
        break
    print(f'我吃了{i}個蘋果')
    i += 1
'''


i = 1
while i <= 5:
    if i == 3:
        print(f'呸！這第{i}個蘋果吃出一個大蟲子，怎麼能吃！')
        i += 1
        # 如果使用 continue，在 continue 之前一定要修改計數器，否則進入死循環。
        continue
    print(f'我吃了{i}個蘋果')
    i += 1



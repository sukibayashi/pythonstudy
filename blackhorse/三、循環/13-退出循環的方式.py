"""
i = 1
while i <= 5:
    if i == 3:
        print('你這遍說的不真誠')
        break
    print('老婆我錯了')
    i += 1
else:
    print('老婆原諒我啦，真開心哈哈哈哈哈')
"""
i = 1
while i <= 5:
    if i == 3:
        print('你這遍說的不真誠')
        i += 1
        continue
    print('老婆我錯了')
    i += 1
else:
    print('老婆原諒我啦，真開心哈哈哈哈哈')
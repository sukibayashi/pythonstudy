import random

player = int(input('請玩家出拳：(1--石頭/2--剪刀/3--布/4--結束)'))
computer = random.randint(1,3)

while player != 4:
    if (player == 1) and (computer == 1) or (player == 2) and (computer == 2) or (player == 3) and (computer == 3):
        if player == 1:
            print('玩家出：石頭')
            print('電腦出：石頭')
            print('平局，再來一局')
        elif player == 2:
            print('玩家出：剪刀')
            print('電腦出：剪刀')
            print('平局，再來一局')
        else:
            print('玩家出：布')
            print('電腦出：布')
            print('平局，再來一局')
        # print(f'玩家出{player}')
        # print(f'電腦出{computer}')
        # print('平局')
    elif (player == 1) and (computer == 2) or (player == 2) and (computer == 3) or (player == 3) and (computer == 1):
        if player == 1:
            print('玩家出：石頭')
            print('電腦出：剪刀')
            print('玩家勝')
        elif player == 2:
            print('玩家出：剪刀')
            print('電腦出：布')
            print('玩家勝')
        else:
            print('玩家出：布')
            print('電腦出：石頭')
            print('玩家勝')
        # print(f'玩家出{player}')
        # print(f'電腦出{computer}')
        # print('玩家勝')
    else:
        if player == 1:
            print('玩家出：石頭')
            print('電腦出：布')
            print('電腦勝')
        elif player == 2:
            print('玩家出：剪刀')
            print('電腦出：石頭')
            print('電腦勝')
        else:
            print('玩家出：布')
            print('電腦出：剪刀')
            print('電腦勝')
        # print(f'玩家出{player}')
        # print(f'電腦出{computer}')
        # print('電腦勝')
    player = int(input('請玩家出拳：(1--石頭/2--剪刀/3--布/4--結束)'))
    computer = random.randint(1, 3)
    continue
else:
    print('歡迎下次再來玩哦!')
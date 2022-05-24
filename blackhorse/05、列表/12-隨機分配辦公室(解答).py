# 1. 準備數據
import random

teachers = ['小紅', '小明', '小張', '小王', '小雪', '小周', '小吳', '小楊']
offices = [[], [], []]

# 2. 分配老師到辦公室 -- 取到每個老師放到辦公室列表 -- 遍歷老師列表數據
for name in teachers:
    # 列表追加數據 -- append(整體) extend(拆開) insert
    # xx[0] -- 不能指定是具體某個下標 -- 隨機
    num = random.randint(0, 2)
    offices[num].append(name)
print(offices)

# 為了更貼合生活， 把各個辦公室子列表加一個辦公室編號 1. 2. 3.
i = 1
# 3. 驗證是否分配成功
for office in offices:
    # 打印辦公室人數 -- 子列表數據的個數 len()
    # 並打印老師的名字
    print(f'{i}號辦公室的人數是{len(office)}, 老師分別是:')
    # print() -- 每個子列表裡面的名字個數不一定 -- 遍歷
    for name in office:
        print(name)
    i += 1
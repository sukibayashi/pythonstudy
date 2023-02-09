# 子串 -- 字符串中的一部分字符
mystr = "hello world and itcast and itheima and Python"

# 1. find()
# print(mystr.find('and')) # 12
# print(mystr.find('and', 15, 30)) # 23 -- 查找從第15行開始30行結束，第一個含有【and】的下標
# print(mystr.find('ands')) # -1 -- 沒有找到該子串

# 2. index()
# print(mystr.index('and')) # 12
# print(mystr.index('ands')) # 12 -- 沒有查找到該子串會直接報錯，而find則是報【-1】

# 3. count()
# print(mystr.count('and',15,30)) # 1 -- 在下標15-30的部分，【and】只出現了一次
# print(mystr.count('and')) # 3 -- 在整個字符串中，【and】出現了3次
# print(mystr.count('ands')) # 0

# 4. rfind()
print(mystr.rfind('and')) # 35 -- 從右邊開始找【and】子串，找到子串後顯示從左到右的下標

# 5. rindex()
print(mystr.rindex('and'))
print(mystr.rindex('ands'))

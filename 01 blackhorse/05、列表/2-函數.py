name_list = ['Tom', 'Lily', 'Lily']

# 1. index()
print(name_list.index('Tom', 0, 2)) # index(數據, 開始位置下標, 結束位置下標)

# 2. count()
print(name_list.count('Lily'))
print(name_list.count('Tony')) # 沒有此子串，顯示0

# 3. len()
print(len(name_list))
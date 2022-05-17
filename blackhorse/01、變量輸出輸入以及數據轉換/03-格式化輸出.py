"""
1. 準備數據
2. 格式化符號輸出數據
"""
age = 18
name = "Tony"
weight = 48.6
stu_id = 19

# 1. 今年我的年齡是x歲 -- 整數 %d
print('今天我的年齡是%d歲' % age)

# 2. 我的名字是x -- 字符串 %s
print('我的名字是%s' % name)

# 3. 我的體重是x公斤 -- 浮點 %f
print('我的體重是%.2f公斤' % weight)

'''
格式化符號高級使用方法
'''
# 4. 我的學號是 x --%d
print('我的學號是%d' % stu_id)

# 4.1 我的學號是019 (當班上學生是100位以上的時候，整合所有號碼位數為3位)
# print('我的學號是%03d' % stu_id)
print('我的學號是%.3d' % stu_id)

# 5. 我的名字是xxx，我的體重是
print('我的名字是%s，我的體重是%.2f公斤' % (name, weight))
# 5.1 我今年多少歲，明年多少歲
print('我今年%d歲，明年%d歲' %(age, age+1))

# 6. 我的名字是x，今年x歲，體重x公斤，學號是x
print('我的名字是%s，今年%d歲，體重%.2f公斤，學號是%.6d' % (name, age, weight, stu_id))

'''
拓展題
'''
# 7. 我的名字是x，今年x歲，體重x公斤（全用%s表示）
print('我的名字是%s，今年%s歲，體重%s公斤' %(name, age, weight))

# 8. 我的名字是x，明年x歲，體重x公斤（用f'{}'格式化）
print(f'我的名字是{name}，明年{age+1}歲，體重{weight}公斤')
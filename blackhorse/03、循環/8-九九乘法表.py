"""
n=0
list1=1
list2=1

while n<9:
    print(f'{list1}*{list2}={list2}')
    list2+=1
    n+=1
"""

"""
n=0
star=1
star2=1
while n<9:
    star3=star*star2
    print(f'{star}*{star2}={star3}')
    star2 += 1
    n+=1
"""

"""
i = 0
value2 = 1
while i < 9:
    n = 0
    value1 = 1
    while n < i+1:
        print(f'{value1}*{value2}={value1 * value2}', end=" ")
        if value2 >= 2:
            value1 += 1
        n += 1
    print()
    value2 += 1
    i += 1
"""

"""
1. 打印一個乘法表達式： x * x = x*x
2. 一行打印多個表達式 -- 一行表達式的個數和行號相等 -- 循環： 一個表達式 -- 不換行
3. 打印多行表達式 -- 循環： 一行表達式 -- 換行
"""

j = 1
while j <= 9:
# 一行的表達式開始
    i = 1
    # i 表示每行裡面的個數，這個數字要和行號相等所以i要和j聯動
    while i <= j:
        print(f'{i} * {j} = {i*j}', end='\t') # \t 製表位Tab，对齐用的
        i += 1
# 一行表達式結束
    print()
    j += 1

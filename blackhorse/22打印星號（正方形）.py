i=0
while i<5:
    n = 0
    while n < 5:
        print("*", end="") # 修改默認的結束符號
        n += 1
    print(end="\n")
    i+=1

# 打印三角形
"""
n = 0
star = '*'
star2 = '*'
while n<5:
    print(star)
    star=''.join((star,star2))
    n+=1
"""

"""
i=0
star = '*'
while i<5:
    print(star)
    star += '*'
    i+=1
"""

# 三角形：每行星星的個數和行號相等
i=0
while i<5:
    n = 0
    while n < i+1:
        print("*", end="") # 修改默認的結束符號
        n += 1
    print(end="\n")
    i+=1
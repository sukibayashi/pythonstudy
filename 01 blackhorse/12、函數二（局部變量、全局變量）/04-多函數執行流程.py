# 1. 聲明全局變量； 2. 定義兩個函數； 3. 函數1修改全局變量； 函數2訪問全局變量

glo_num = 0


def test1():
    global glo_num
    glo_num = 100


def test2():
    print(glo_num)


print(glo_num)  # 0, 因為修改的函數沒有執行
test1()  # 如果沒有調用或者執行test1(), test2()中的glo_num還是為0
test2()  # 100，因為先調用了函數1
print(glo_num)

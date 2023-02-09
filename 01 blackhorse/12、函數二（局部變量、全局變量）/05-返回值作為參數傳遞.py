# 1. 定義兩個函數； 2. 函數一返回值為50； 函數二把返回值50作為參數傳入（定義函數二）

def test1():
    return 50


def test2(num):
    print(num)


# 先得到函數一的返回值，再把這個返回值傳入到函數二
result = test1()
test2(result)

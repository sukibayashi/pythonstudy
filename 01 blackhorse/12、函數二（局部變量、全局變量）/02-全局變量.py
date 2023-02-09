# 聲明全局變量：函數體內外部都能訪問
a = 100


def testA():
    print(a)


def testB():
    print(a)


testA()
testB()

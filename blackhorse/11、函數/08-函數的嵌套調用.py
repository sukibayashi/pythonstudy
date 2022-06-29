# 兩個函數 testA 和 testB --- 在 A 裡面嵌套調用 B

# B 函數
def testB():
    print('B函數開始')
    print('B函數開始')
    print('B函數結束')


# A 函數
def testA():
    print('A函數開始----')
    # 嵌套調用 B
    testB()
    print('A函數結束----')


testA()

# 1. 打印一條橫線

def print_line():
    print('-' * 20)


# print_line()

# 2. 函數嵌套調用，實現多條橫線
def print_line2(num):
    """
    打印橫線
    num: 打印橫線的數量
    """
    i = 0
    while i < num:
        print('-' * 20)
        i += 1


print_line2(5)

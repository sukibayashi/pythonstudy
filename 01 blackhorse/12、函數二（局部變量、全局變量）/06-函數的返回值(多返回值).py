# 需求：一個函數有兩個返回值1和2

# 一個函數如果有多個return不能都執行，只執行第一個return，無法做到一個函數多個返回值。
# def return_num():
#     return 1
#     return 2
#
#
# result = return_num()
# print(result)

# 一個函數多個返回值的寫法
def return_num():
    # return 1, 2  # 返回的是元祖
    # return [1, 2]  # 返回的是列表
    # return {1, 2}  # 返回的是集合
    return {'name': 'Python', 'age': 30}  # 返回的是字典


result = return_num()
print(result)

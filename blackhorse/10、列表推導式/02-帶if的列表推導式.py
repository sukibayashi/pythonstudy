# 需求：0-10偶數數據的列表
# 1. 簡單的列表推導式 range 步長
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 2. for循環加if，創建有規律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)

# 3. 把for循環配合if的代碼，改寫 帶if的列表推導式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
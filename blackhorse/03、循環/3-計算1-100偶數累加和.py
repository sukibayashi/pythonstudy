'''
# 第一種方法
i=2
result=0

while i<=100:
    result+=i
    i+=2
print(result)
'''

# 第二種方法
'''
1. 準備累加的數字 開始1 結束100 增量1
2. 準備保存結果的變量 result
3. 循環加法運算 -- 如果是偶數才加法運算 --和2去餘數為0
4. 輸出結果
5. 驗證結果
'''

i = 1
result = 0
while i<=100:
    # 條件語句 -- if
    if i % 2 == 0:
        # 加法運算
        result += i
    i += 1
print(result)

print(11%2)

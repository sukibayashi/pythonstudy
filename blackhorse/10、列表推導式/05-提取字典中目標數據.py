counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 1. 需求：提取電腦台數大於等於200
# 獲取所有鍵值對數據，判斷v值大於等於200返回，字典
count1 = {k: v for k, v in counts.items() if v >= 200}
print(count1)

import datetime
import json
import typing

import pandas as pd
import requests

# 備註，新版本的Edge需要在F12→Payload選項卡找到get資料
URL = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={}&type=ALLBUT0999&_={}"

HEADER = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Host": "www.twse.com.tw",
    "Referer": "https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

def crawler(parameters:typing.Dict[str, str]) -> pd.DataFrame:
    # get()方法是 Python 字典對象中的內置方法，用於獲取字典中鍵對應的值
    crawler_date = parameters.get("crawler_date", "")
    crawler_date = crawler_date.replace("-", "")
    # 统一性： Unix 时间戳是一个全球通用的标准，在任何地方都可以使用，不存在因地区不同而造成的误差。
    # Unix 时间戳是一个整数，简单易懂，易于存储和使用
    crawler_timestamp = int(datetime.datetime.now().timestamp())
    
    # .format 是 Python 中字符串格式化的方法，用于填充字符串中的占位符
    resp = requests.get(
        url=URL.format(crawler_date, crawler_timestamp), headers=HEADER
    )
    
    columns = [
        "stock_id",
        "stock_name",
        "open",
        "max",
        "min",
        "close",
    ]
    
    # Requests 库的属性，用于表示请求是否成功
    if resp.ok:
        resp_data = json.loads(resp.text)
        data = pd.DataFrame(resp_data["data9"])
        data = data[[0, 1, 5, 6, 7, 8]]
        data.columns = columns
        data["date"] = parameters.get("crawler_date", "")
    else:
        data = pd.DataFrame()
    return data
    
if __name__ == "__main__":
    parameters = {
        "crawler_data": "2023-02-07"
    }
    data = crawler(parameters)
    print(data)
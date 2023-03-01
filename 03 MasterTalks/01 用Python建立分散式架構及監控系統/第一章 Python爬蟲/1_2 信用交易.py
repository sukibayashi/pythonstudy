import datetime
import json
import typing

import pandas as pd
import requests

URL = "https://www.twse.com.tw/exchangeReport/MI_MARGN?response=json&date={}&selectType=ALL&_={}"

HEADER = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Host": "www.twse.com.tw",
    "Referer": 'https://www.twse.com.tw/zh/page/trading/fund/T86.htmlsec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    "sec-ch-ua": '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78",
    "X-Requested-With": "XMLHttpRequest",
}

def crawler(parameters:typing.Dict[str, str]) -> pd.DataFrame:
    crawler_date = parameters.get("crawler_date","")
    crawler_date = crawler_date.replace("-","")
    crawler_timestamp = int(datetime.datetime.now().timestamp())
    
    resp = requests.get(
        url=URL.format(crawler_date, crawler_timestamp), headers=HEADER
    )
    
    columns = [
        "stock_id",
        "stock_name",
        "MarginPurchaseBuy",
        "MarginPurchaseSell",
        "MarginPurchaseCashRepayment",
        "MarginPurchaseYesterdayBalance",
        "MarginPurchaseTodayBalance",
        "MarginPurchaseLimit",
        "ShortSaleBuy",
        "ShortSaleSell",
        "ShortSaleCashRepayment",
        "ShortSaleYesterdayBalance",
        "ShortSaleTodayBalance",
        "ShortSaleLimit",
        "OffsetLoanAndShort",
        "Note",
    ]
    
    if resp.ok:
        resp_data = json.loads(resp.text)
        data = resp_data.get("data", "")
        data = pd.DataFrame(data, columns=columns)
        data["date"] = parameters.get("crawler_date", "")
    else:
        data = pd.DataFrame(columns=columns)
    return data
    
if __name__ == "__main__":
    parameters = {
        "crawler_date": "2023-02-07",
    }
    data = crawler(parameters)
    print(data)
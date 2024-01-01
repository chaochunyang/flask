from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import json
import requests
import pandas as pd
import pprint
url_db = "mongodb+srv://paul10301004:qufmyb-7cingo-dyxfeQ@cluster0.hwpamb1.mongodb.net/?retryWrites=true&w=majority"

# 連接到 MongoDB
client = MongoClient(url_db, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client["cloudData"]
collection = db["ETF_DIVIDEND"]
# pprint.pprint(client.cloudData.ETF)

for data in collection.find({'ETF_ID': '00929'}):
    print(data)

collection.insert_one(
    {
    "ETF_ID" : "00919",
    "ETF_NAME" : "群益台灣精選高息",
    "配息" : 1.63,
    "殖利率" : 7.33,
    "2022" : 0.55,
    "2021" : 0,
    "2020" : 0,
    "2019" : 0,
    "2018" : 0,
    "配息頻率" : "季配息"
    }
)


# 插入API 資料
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockInfoWithWarrant",
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRlIjoiMjAyMy0xMi0wOSAxNTo1NTowNSIsInVzZXJfaWQiOiJwYXVsMTAzMDEwMDQiLCJpcCI6IjEyMy4yNDAuODYuMTQ1In0.LPC2l_1fZkuPobWRKZrZozn70I7ac6cmkxeo1l7yIE0"
# }

# resp = requests.get(url, params=parameter)
# data = resp.json()
# etf_info = pd.DataFrame(data["data"])

# # 插入 ETF 數據到 MongoDB
# etf_records = etf_info.to_dict(orient='records')
# collection.insert_many(etf_records)

# 關閉 MongoDB 連接
client.close()
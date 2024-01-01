import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connet_db():
    url_db = "mongodb+srv://paul10301004:qufmyb-7cingo-dyxfeQ@cluster0.hwpamb1.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(url_db, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client

def get_collection(client, db_name='cloudData', col_name='ETF_COMPONENTS'):
    db = client[db_name]
    collection = db[col_name]
    cursor = collection.find()
    df = pd.DataFrame(list(cursor))
    client.close()
    return df

def get_etf_components(etf_id,col_name):
    client = connet_db()
    df = get_collection(client,col_name=col_name)
    flitered_df = df[df['ETF_ID']==etf_id]
    return flitered_df

result = get_etf_components('00929','ETF_COMPONENTS')
result[['ETF_ID','name','weighting']]
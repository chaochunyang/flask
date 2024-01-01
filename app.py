from flask import Flask, render_template, request, url_for,redirect,session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import json

# url_db = "mongodb+srv://paul10301004:qufmyb-7cingo-dyxfeQ@cluster0.hwpamb1.mongodb.net/?retryWrites=true&w=majority"
url_db = "mongodb+srv://paul10301004:qufmyb-7cingo-dyxfeQ@cluster0.hwpamb1.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
app.secret_key = "dontguessmysecretkey"

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/etfTables", methods=['GET','POST'])
def get_table_data():
    stock1 = request.args.get('stock1', session.get('stock1', '0050'))
    stock2 = request.args.get('stock2', session.get('stock2', '006208'))
    stock3 = request.args.get('stock3', session.get('stock3', '00881'))
    
    if request.method == 'POST':
        stock1 = request.form['stock1']
        stock2 = request.form['stock2']
        stock3 = request.form['stock3']
        
        session['stock1'] =stock1
        session['stock2'] =stock2
        session['stock3'] =stock3

        return redirect(url_for('get_table_data',stock1=stock1,stock2=stock2,stock3=stock3))
    
    if stock1 or stock2 or stock3:
        pass
    else:
        stock1 = session.get('stock1', default='0050')
        stock2 = session.get('stock2', default='006208')
        stock3 = session.get('stock3', default='00881')

    if stock1 or stock2 or stock3:
        etf1_components = collect_components.find({'ETF_ID': stock1})
        etf2_components = collect_components.find({'ETF_ID': stock2})
        etf3_components = collect_components.find({'ETF_ID': stock3})
        
        etf1_dividend = collect_dividend.find({'ETF_ID': stock1})
        etf2_dividend = collect_dividend.find({'ETF_ID': stock2})
        etf3_dividend = collect_dividend.find({'ETF_ID': stock3})
        
        etf1_operate = collect_operate.find({'ETF_ID': stock1})
        etf2_operate = collect_operate.find({'ETF_ID': stock2})
        etf3_operate = collect_operate.find({'ETF_ID': stock3})
        
        etf1_value = collect_value.find({'ETF_ID': stock1})
        etf2_value = collect_value.find({'ETF_ID': stock2})
        etf3_value = collect_value.find({'ETF_ID': stock3})

        etf1_name = collect_name.find({'stock_id': stock1})
        etf2_name = collect_name.find({'stock_id': stock2})
        etf3_name = collect_name.find({'stock_id': stock3})
        
    else:
        etf1_components = []
        etf2_components = []
        etf3_components = []
        etf1_dividend = []
        etf2_dividend = []
        etf3_dividend = []
        etf1_operate = []
        etf2_operate = []
        etf3_operate = []
        etf1_value = []
        etf2_value = []
        etf3_value = []
        etf1_name = []
        etf2_name = []
        etf3_name = []

    options_data = ["0050","0056","006208","00713","00878","00881","00882","00919","00929"]

    return render_template('etfTables.html',
                           etf1_components=etf1_components, 
                           etf2_components=etf2_components,
                           etf3_components=etf3_components,
                           etf1_dividend = etf1_dividend,
                           etf2_dividend = etf2_dividend,
                           etf3_dividend = etf3_dividend,
                           etf1_operate = etf1_operate,
                           etf2_operate = etf2_operate,
                           etf3_operate = etf3_operate,
                           etf1_value = etf1_value,
                           etf2_value = etf2_value,
                           etf3_value = etf3_value,
                           etf1_name = etf1_name,
                           etf2_name = etf2_name,
                           etf3_name = etf3_name,
                           options=options_data,
                           stock1=stock1,
                           stock2=stock2,
                           stock3=stock3
                           )

@app.route("/etfTables/<etf1>/<etf2>/<etf3>", methods=['GET','POST'])
def direct_table_data(etf1,etf2,etf3):
    stock1 = etf1
    stock2 = etf2
    stock3 = etf3

    return redirect(url_for('get_table_data',stock1=stock1,stock2=stock2,stock3=stock3))

def connet_db(url_db):
    client = MongoClient(url_db, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client

@app.route("/etfCharts", methods=['GET','POST'])
def get_chart_data():
    if request.method == 'POST':
        stock1 = request.form['stock1']
        stock2 = request.form['stock2']
        stock3 = request.form['stock3']

        session['stock1'] =stock1
        session['stock2'] =stock2
        session['stock3'] =stock3

        return redirect(url_for('get_chart_data'))
    
    stock1 = session.get('stock1', default='00878')
    stock2 = session.get('stock2', default='00919')
    stock3 = session.get('stock3', default='00929')

    if stock1 or stock2 or stock3:
        etf1_price = collect_price.find({'ETF_ID':stock1})
        etf1_price_list = list(etf1_price)
        etf1_list = [{'x': record['date'], 'y': record['close']} for record in etf1_price_list]
        etf1_list = sorted(etf1_list, key=lambda x: x['x'])
        # for record in result_list:
        #     print(record)
        etf2_price = collect_price.find({'ETF_ID':stock2})
        etf2_price_list = list(etf2_price)
        etf2_list = [{'x': record['date'], 'y': record['close']} for record in etf2_price_list]
        etf2_list = sorted(etf2_list, key=lambda x: x['x'])
        
        etf3_price = collect_price.find({'ETF_ID':stock3})
        etf3_price_list = list(etf3_price)
        etf3_list = [{'x': record['date'], 'y': record['close']} for record in etf3_price_list]
        etf3_list = sorted(etf3_list, key=lambda x: x['x'])
    
    else:
        etf1_list = []
        etf2_list = []
        etf3_list = []
    
    options_data = ["0050","0056","006208","00713","00878","00881","00882","00919","00929"]


    return render_template('etfCharts.html',
                           etf1 = str(stock1),
                           etf2 = str(stock2),
                           etf3 = str(stock3),
                           etf1_price_json = json.dumps(etf1_list),
                           etf2_price_json = json.dumps(etf2_list),
                           etf3_price_json = json.dumps(etf3_list),
                           options=options_data
                           )


if __name__ == "__main__":
    client = connet_db(url_db)
    db = client['cloudData']
    collect_components = db['ETF_COMPONENTS']
    collect_dividend = db['ETF_DIVIDEND']
    collect_operate = db['ETF_OPERATE']
    collect_value = db['ETF_VALUE']
    collect_name = db['ETF']
    collect_price = db['ETF_PRICE']

    app.run(debug=True)
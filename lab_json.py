from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():  
    return "Hello! Flask!"

def read_data():
    data = []
    with open("./data/pvuv.txt") as fin:
        for line in fin:    
            line = line[:-1]
            pdate, pv, uv = line.split("\t")
            data.append((pdate, pv, uv))
    return data

@app.route('/data')
def get_table():
    data = read_data()
    return json.dumps(data)

if __name__ == '__main__':
    app.run()

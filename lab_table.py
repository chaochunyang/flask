from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Flask!"

@app.route('/data')
def get_table():
    data = []
    with open("./data/pvuv.txt") as fin:
        for line in fin:
            line = line[:-1]
            pdate, pv, uv = line.split("\t")
            data.append((pdate, pv, uv))
    return render_template("pvuv.html",data=data)

if __name__ == '__main__':
    app.run()

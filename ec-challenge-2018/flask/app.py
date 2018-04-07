from flask import Flask, render_template, Markup,request,jsonify

app = Flask(__name__)


@app.route("/")
def main():
    labels = ["#metoo", "#china", "#usa", "#puppy", "#look", "#rest", "#coffe", "#nerd", "#nerd", "#nerd"]
    values = [10, 9, 8, 7, 6, 4, 7, 8, 1, 6]
    return render_template('index.html', values=values, labels=labels)


@app.route('/metoo')
def metoo():
    with open("dane.txt", 'r') as f:
        lines = f.readlines()
        language = [line.split(';')[0] for line in lines]
        values = [float(line.split(';')[1]) for line in lines]
    return render_template('index.html', values=values, labels=language)


@app.route('/table')
def table():
    with open("dane2.txt", 'r', encoding="utf8") as f:
        lines = f.readlines()
        key = [line.split(';')[0] for line in lines]
        value = [int(line.split(';')[1]) for line in lines]
    dic = dict(zip(key, value))
    return render_template('table.html', result=dic)


@app.route('/chart')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)


@app.route('/send',methods = ['POST', 'GET'])
def send():
    FILES = {'realtime_num':'real_time/tagData.txt'}
    import json
    with open( '../data/'+FILES[request.args['type']], 'r') as f:
        lines = f.read().splitlines()
        last_lines = lines[-10:-1]

    datat = []
    for line in last_lines:
        x,data=line.split('=')
        data=eval(data)
        datat.append(data)

    return jsonify(datat)

if __name__ == "__main__":
    app.run(debug=True)

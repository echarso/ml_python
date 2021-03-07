#! /usr/bin/env python
import json
import json
from flask import Flask, request
from flask import render_template
from controller import Controller

app = Flask(__name__)
con = Controller();


@app.route("/")
def root():
    print('application started in returning root ')
    return render_template('index.html')



@app.route("/forecast")
def forecast():
    print('forecast api')

    print(request.data)
    data = json.loads(request.data)
    ret = con.predict()
    return ret


if __name__ == '__main__':
    print('application started')
    app.run(host='127.0.0.1', port=8080, debug=True)

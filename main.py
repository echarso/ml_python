#! /usr/bin/env python
import json
from flask import Flask
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
    ret = con.predict([{5:'6'}])
    return ret


if __name__ == '__main__':
    print('application started')
    app.run(host='127.0.0.1', port=8080, debug=True)

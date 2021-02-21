#! /usr/bin/env python
import json
from flask import Flask
from flask import render_template
from controller import Controller

app = Flask(__name__)
con = Controller();


@app.route("/")
def forecast():
    return app.send_static_file('templates/index.html')



@app.route("/forecast")
def forecast():
    ret = con.predict()
    return ret


if __name__ == '__main__':
    print('application started')
    app.run(debug=True, port=8080)

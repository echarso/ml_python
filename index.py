#! /usr/bin/env python
import json
from flask import Flask
from flask import render_template
from controller import Controller

app = Flask(__name__)
con = Controller();


@app.route("/")
def get_search():
    print "==================="
    ret = con.predict()
    print [row[0] for row in ret]
    print "==================="

    return json.dumps([row[0] for row in ret])


@app.route("/forecast")
def forecast():
    print "==================="
    ret = con.predict()
    print [row[0] for row in ret]
    print "==================="

    return json.dumps([row[0] for row in ret])

if __name__ == '__main__':
    app.run(debug=True)

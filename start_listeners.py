#!/usr/bin/python3

from flask import Flask
import requests


#import Utils.utils as u

requests.post("34.210.186.181")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
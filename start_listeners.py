#!/usr/bin/python3

from flask import Flask, abort, request
import json
import mongodb

# App that run on server.
# Get data from reporter.
# Store data on DB.

class http_listener:
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def parse_request():
        if request.method == 'POST':
            print(str(request.form['ph']))
        return "OK"

    if __name__ == '__main__':
        app.run()


a = http_listener()

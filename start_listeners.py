#!/usr/bin/python3

from flask import Flask, abort, request
import json

class http_listener:
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def parse_request():
        if not request.json:
            abort(400)
        print(request.json)
        return json.dumps(request.json)

    if __name__ == '__main__':
        app.run()


a = http_listener()
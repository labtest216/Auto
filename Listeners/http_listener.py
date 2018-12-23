#!/usr/bin/python3

from flask import Flask
import Utils.utils as u

app = Flask(__name__)

class HttpListener:
    cfg = {"a": 1}



    @app.route("/get/temperature")
    def get_temperature():
        return u.dprint("hh")
        #return "hh"


if __name__ == '__main__':
    app.run()


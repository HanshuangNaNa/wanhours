#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月08日 星期四 20时30分21秒
# File Name: api.py
# Description:
"""
import logging
from flask import Flask
from flask.ext import restful

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)


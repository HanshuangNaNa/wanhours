#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月09日 星期五 21时14分25秒
# File Name: hello.py
# Description:
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index ():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s</h1>' % name

if __name__ == '__main__':
    app.run(debug = True)

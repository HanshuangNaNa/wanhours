#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月23日 星期五 21时15分53秒
# File Name: hello.py
# Description:
"""
from flask import Flask,render_template
from flask import request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    name = '<p>'+name+'</p>'
    return render_template('user.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)

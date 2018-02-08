#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月08日 星期四 20时34分15秒
# File Name: hello.py
# Description:
"""
import logging
from flask import Flask
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/user/<username>')
def hello_user(username):
    return 'Hello {}'.format(username)

@app.route('/post/<int:postid>')
def showpost(postid):
    return 'Post is {}'.format(postid)

@app.route('/project/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'This about'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)



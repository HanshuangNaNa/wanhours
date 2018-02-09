#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月09日 星期五 19时55分45秒
# File Name: flasky.py
# Description:
"""
import logging
import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

app = Flask(__name__)
app.config,from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        pass

if __name__ == '__main__':
    app.run()

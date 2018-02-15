#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月14日 星期三 16时52分54秒
# File Name: api.py
# Description:
"""
import logging
from flask import Flask,request
from flask.ext.restful import Resource,Api

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')
app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self,todo_id):
        return {todo_id:todos[todo_id]}

    def put(self,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}

api.add_resource(TodoSimple,'/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
    app.run

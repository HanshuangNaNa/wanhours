#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月14日 星期三 16时52分54秒
# File Name: api.py
# Description:
"""
import logging
from flask import Flask,request,jsonify,abort,make_response

app = Flask(__name__)

tasks = [
        {
            'id':1,
            'title':'coding',
            'description':'一万个小时',
            'done':False
        },
        {
            'id':2,
            'title':'写商城',
            'description':'写接口',
            'done':False
        }
        ]

@app.route('/todo/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/todo/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t : t['id'] == task_id,tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

@app.route('/todo/tasks',methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
            'id':tasks[-1]['id']+1,
            'title':request.json['title'],
            'description':request.json.get('description',""),
            'done':False
            }
    tasks.append(task)
    return jsonify({'task':task}),201

if __name__ == '__main__':
    app.run(debug=True)



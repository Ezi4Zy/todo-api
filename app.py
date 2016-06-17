#!flask/bin/python
# -*- coding: utf-8 -*-
# @Author: Ezi
# @Email:  Ezi4zy@163.com
# @File:   app.py
# @Date:   2016-06-17 14:54:40

from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Chesse, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn python',
        'description': u'Need to find a good python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)

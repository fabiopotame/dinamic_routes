from flask import Flask, request, jsonify
import os
import config
import importlib
import sqlite3
import logging
import sys

app = Flask(__name__)
logging.basicConfig(filename='app.log',level=logging.INFO)

# peewee
@app.route('/<control>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<control>/<method>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<control>/<method>/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

def route(control, method='index', id=None):
    # try:
        controller = load_controller(control)
        response = routing(request.method, controller, method, id, request.form)
        return response, 200

    # except Exception as e:
    #     return jsonify({'code': 404, 'message': 'Not found!'}), 404


def routing(verb, controller, method, id, form):
    return load_method(verb, controller, method, id, form)


def load_controller(control):
    try:
        controller = importlib.import_module('controller.' + control)
        return controller

    except Exception:
        return 'Controller not found!'


def load_method(verb, controller, method, id=None, form=None):
    return getattr(controller, method)(verb, id, form)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
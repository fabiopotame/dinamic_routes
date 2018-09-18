from flask import jsonify
import os

def index(id=None, form=None):
    return 'customer'


def insert(id, form):
    return jsonify(id, form)


def edit(id, form):
    return jsonify(id, form)


def delete(id, form=None):
    return jsonify(id, form)
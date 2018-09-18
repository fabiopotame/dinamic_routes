from flask import jsonify

def index(verb, id=None, form=None):
    return verb + 'cars'


def insert(verb, id, form):
    return verb + 'cars'


def edit(verb, id, form):
    return jsonify(id, form)


def delete(verb, id, form=None):
    return jsonify(id, form)
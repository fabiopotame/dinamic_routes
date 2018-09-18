from flask import jsonify

def index(verb, id, form):
    return jsonify(verb, 'teste2', {'teset'}})


def insert(verb, id, form):
    return verb + 'aquii'


def edit(verb, id, form):
    return jsonify(id, form)


def delete(verb, id, form=None):
    return jsonify(id, form)
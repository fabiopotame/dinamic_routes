from flask import jsonify

def index(verb, id, form):
    return jsonify(verb, id, form)


def insert(verb, id, form):
    return verb + 'partner'


def edit(verb, id, form):
    return jsonify(id, form)


def delete(verb, id, form):
    return jsonify(id, form)
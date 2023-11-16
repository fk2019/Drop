#!/usr/bin/python3
"""New view for  User objects"""
from api.v1.views import app_views
from flask import abort, request, make_response, jsonify
from models import storage
from models.user import User


@app_views.route('/users', strict_slashes=False)
def users():
    """Retrieve list of all User objects"""
    result = []
    obj = storage.all(User)
    if obj is None:
        abort(404)
    for am in obj.values():
        result.append(am.to_dict())
    return (jsonify(result))


@app_views.route('/users/<string:user_id>', strict_slashes=False)
def user(user_id):
    """Retrieve a User object"""
    obj = storage.get(User, user_id)
    if obj:
        return obj.to_dict()
    else:
        abort(404)

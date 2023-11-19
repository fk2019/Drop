#!/usr/bin/python3
"""New view for  User objects"""
from api.v1.views import app_views
from flask import abort, request, make_response, jsonify
from models import storage
from models.user import User
from models.post import Post


@app_views.route('/users/<string:user_id>/sent', strict_slashes=False)
def sent_posts(user_id):
    """Retrieve list of all sent Post objects"""
    result = []
    obj = storage.get(User, user_id)
    if obj is None:
        abort(404)
    for post in obj.sent_messages:
        result.append(post.to_dict())
    return (jsonify(result))

@app_views.route('/users/<string:user_id>/received', strict_slashes=False)
def received_posts(user_id):
    """Retrieve list of all received Post objects"""
    result = []
    obj = storage.get(User, user_id)
    if obj is None:
        abort(404)
    for post in obj.received_messages:
        result.append(post.to_dict())
    return (jsonify(result))


@app_views.route('/posts/<string:post_id>', strict_slashes=False)
def post(post_id):
    """Retrieve a User object"""
    obj = storage.get(Post, post_id)
    if obj:
        return obj.to_dict()
    else:
        abort(404)

#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.user import User
from models.post import Post
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route('/', strict_slashes=False)
def chat():
    users = storage.all(User).values()
    users = sorted(users, key=lambda k:k.updated_at)

    return render_template('1-chat.html', users=users, cache_id=uuid.uuid4())

if __name__ == "__main__":

    app.run(host='0.0.0.1', port=3000)

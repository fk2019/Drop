#!/usr/bin/python3
from models.user import User
from models.post import Post
from models import storage


def main():
    kwargs = { "first_name": "shin", "last_name": "shinigami", "email": "fkmuiruri8@gmail.com", "password": "shin86"}
    kwargs2 = {"first_name": "chopper", "last_name": "tony tony", "email": "chopperdoc@north.com", "password": "reindeer"}
    kwargs3 = {"first_name": "john", "last_name": "wick", "email": "puppy@continental.org", "password": "puppy"}

    posts = {"title": "introduction to DSA", "content": "DSA may sound provocative on first encounter. However, ALX made it appear easy, of course after working really hard."}
    #kwargs4 = {"first_name": "ragna", "last_name": "crimson", "email": "ragna@oblivion.society", "password": "dragonhunter01", "posts": [Post(**posts)]}
    post = Post(**posts)
    post.save()
    print(post)
    a = storage.all()
    #print(a)





main()

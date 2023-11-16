#!/usr/bin/python3
from models import storage
from models.post import Post
from models.user import User

def main():
    f = storage._DBStorage__session.query(User).first()
    print("first ob:", f.id)

    d = storage._DBStorage__session.query(Post).first()
    print(d)
    d.delete()
    f.save()
    print_post(f.posts)
    #d.delete()

def print_post(post):
    ids= []
    for p in post:
        print(p.id)
        ids.append(p)
    return ids


main()

#!/usr/bin/python3
from models.user import User
from models.post import Post
from models import storage
from datetime import datetime

def main():
    post3 = {'title': 'History', 'content': 'History is the study of past events, particularly in human affairs and societies.'}
    post4 = {'title': 'Science and Technology', 'content': 'Science is the systematic study of the natural world, and technology refers to the application of scientific knowledge for practical purposes.'}
    f = storage._DBStorage__session.query(User).first()
    users = storage.all(User).values()
    up = {"last_name": "Yonko"}
    p = f.posts[0]
    u = storage.get(User, f.id)
    p = []
    for po in u.posts:
        p.append(po.to_dict())
    posts = []
    us = sorted(users, key=lambda k:k.first_name)
    for user in us:
        posts.append([user, sorted(user.posts, key=lambda k:k.title)])
    for u in posts:
        print("fname", u[0].first_name)
        for p in u[1]:
            print("title", p.title)
    
    
    #print(p.to_dict(), p.title)


def update(f, dic):
    for key, val in dic.items():
        if key not in ["id", "created_at"]:
            setattr(f, key, val)
            f.updated_at = datetime.now()

    f.save()


def print_post(post):
    ids= []
    for p in post:
        print(p.id)
        ids.append(p)
    return ids

main()

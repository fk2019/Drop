#!/usr/bin/python3
from models.user import User
from models.post import Post
from models import storage

def main():
    post3 = {'title': 'History', 'content': 'History is the study of past events, particularly in human affairs and societies.'}
    post4 = {'title': 'Science and Technology', 'content': 'Science is the systematic study of the natural world, and technology refers to the application of scientific knowledge for practical purposes.'}
    f = storage._DBStorage__session.query(User).first()
    f.posts.extend([Post(**post3), Post(**post4)])
    f.save()
    print_post(f.posts)

def print_post(post):
    ids= []
    for p in post:
        print(p.id)
        ids.append(p)
    return ids

main()

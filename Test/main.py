#!/usr/bin/python3
from models.user import User
from models.post import Post
from models import storage
from datetime import datetime
import time

ftime = "%H:%M:%S  %d %b %y"
kwargs = { "user_name": "shin", "email": "fkmuiruri8@gmail.com", "password": "shin86"}
kwargs2 = {"user_name": "chopper", "email": "chopperdoc@north.com", "password": "reindeer"}
kwargs3 = {"user_name": "john", "email": "puppy@continental.org", "password": "puppy"}
kwargs4 = {"user_name": "ragna", "email": "ragna@oblivion.society", "password": "dragonhunter01"}

def create_users():
    users = [kwargs, kwargs2, kwargs3, kwargs4]
    us = []
    for user in users:
        u = User(**user)
        u.save()
        us.append(u)
    return us
def main():

    post = {"title": "introduction to DSA", "content": "DSA may sound provocative on first encounter. However, ALX made it appear easy, of course after working really hard."}

    post2 = {'title': 'Anime', 'content': 'Anime is a style of animation that originated in Japan and has become popular worldwide.'}
    post3 = {'title': 'History', 'content': 'History is the study of past events, particularly in human affairs and societies.'}
    post4 = {'title': 'Science and Technology', 'content': 'Science is the systematic study of the natural world, and technology refers to the application of scientific knowledge for practical purposes.'}
    users = create_users()
    print(users)
    #print(users)
    #f_user = users[0]
    #us2 = users[1]
    #msg = {"content": "Hello", "sender_id": f_user, "receiver_id": us2.id}
    #msg2 = {"content": "Going out?", "sender_id": f_user, "receiver_id": us2.id}
    #msg3 = {"content": "Hi, yeah. When do we meet?", "sender_id": us2.id, "receiver_id": f_user.id}

    #print(f_user, us2)
    #f_user.sent_messages.extend([Post(**msg), Post(**msg2)])
    #f_user.save()
main()

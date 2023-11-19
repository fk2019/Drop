#!/usr/bin/python3
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    if models.storage_t == "db":
        __tablename__ = "users"
        user_name = Column(String(128), nullable=False)
        #last_name = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        profile_photo = Column(String(123), default='images/dog.jpg')

        sent_messages = relationship('Post', backref='sender', foreign_keys='Post.sender_id')
        received_messages = relationship('Post', backref='receiver', foreign_keys='Post.receiver_id')

    else:
        first_name = ""
        last_name = ""
        email = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = "posts"
        #title = Column(String(128), nullable=False)
        content = Column(String(1024), nullable=False)
        sender_id = Column(String(60), ForeignKey('users.id', ondelete= 'CASCADE'))
        receiver_id = Column(String(60), ForeignKey('users.id', ondelete= 'CASCADE'))
    else:
        first_name = ""
        last_name = ""
        email = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#!/usr/bin/env python
# coding=utf-8
from sqlalchemy import Column, String ,  DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Notification(Base):

    """the class map to table of crystal.notifications"""

    __tablename__ = 'notifications'

    url = Column(String, primary_key=True)
    title = Column(String)
    college = Column(String)
    speaker = Column(String)
    venue = Column(String)
    time = Column(DATETIME)
    notify_time = Column(DATETIME)

        

#!/usr/bin/env python
# coding=utf-8
from sqlalchemy import Column, String ,  DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Seed(Base):

    """the class map to table of crystal.seeds"""
    __tablename__ = 'seeds' 

    start_url = Column(String, primary_key=True)
    college = Column(String)
    url_xpath = Column(String)
    word = Column(String)
    title = Column(String)
    speaker = Column(String)
    venue = Column(String)
    time = Column(String) 
    text_xpath = Column(String)

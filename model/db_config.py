#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis

# 初始化数据库连接:
engine = create_engine('mysql://root:root@localhost:3306/crystal?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

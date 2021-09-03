#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 22:29
# @Author  : LXH
# @File    : 09 redis.py

import  redis

r = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)
r.rpush('liset1', 'foo', 'aar')
m = r.lrange('liset1', 0, -1)
print(m)
print(type(m))
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 20:04
# @Author  : LXH
# @File    : log.py

import logging

class log():
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format= '%(asctime)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H %M %S',
                            filename='./../report/log/21-2-1.log',
                            filemode='w'
                            )
    def add_log(self,page,func):
        out_str = page+':'+func
        logging.info(out_str)
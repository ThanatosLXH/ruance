#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 22:15
# @Author  : LXH
# @File    : run_sou.py

import unittest

suite = unittest.defaultTestLoader.discover('./../case_manage/', pattern='test_baidu_*.py')







if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
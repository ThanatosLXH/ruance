#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 22:15
# @Author  : LXH
# @File    : run_sou.py

import unittest

suite = unittest.defaultTestLoader.discover('./../case_manage/', pattern='test_baidu_news.py')







if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    runner = htmltestreport.HTMLTestReport('./../report/html/report.html', title='百度新闻搜索测试报告', description='带饼图 带详情')
    runner.run(suite)
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 22:15
# @Author  : LXH
# @File    : run_sou.py

import unittest
import htmltestreport,datetime
from utils.init_folder import init_html_folder

suite = unittest.defaultTestLoader.discover('./../case_manage/', pattern='test_baidu_search.py')







if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    date_time = datetime.datetime.now()
    date = date_time.strftime('%y-%m-%d')
    report_time = date_time.strftime('%H%M%S')
    init_html_folder(date)
    runner = htmltestreport.HTMLTestReport('./../report/html/'+date+'/'+report_time+'report.html', title='百度搜索测试报告', description='带饼图 带详情')
    runner.run(suite)
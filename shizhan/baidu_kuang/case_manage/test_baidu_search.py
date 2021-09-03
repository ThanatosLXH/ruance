#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 21:58
# @Author  : LXH
# @File    : test_baidu_search.py

import unittest, time, ddt
from selenium import webdriver
from utils.excel_read import ReadExcel
from utils.log import log

excel_path = './../data_manage/test.xlsx'
sheetName = 'data_sou'
excel = ReadExcel(excel_path,sheetName)
chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
@ddt.ddt
class Test_baidu_Search(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.log = log()
    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()
    def setUp(self) -> None:
        self.driver.get('http://www.baidu.com')
        time.sleep(1)
    def tearDown(self) -> None:
        pass
    @ddt.data( * excel.getDataFromSheet())
    def test_sou(self, data):
        try:
            self.driver.find_element_by_id('kw').send_keys(data)
            time.sleep(2)
            self.driver.find_element_by_id('su').click()
            time.sleep(4)
            self.assertEqual(data+'_百度搜索', self.driver.title)
        except AssertionError as e:
            self.log.add_log(data,format(e))
            self.assertEqual(data + '_百度搜索', self.driver.title)
        else:
            self.log.add_log(data,'用例执行成功')

if '__name__' == '__main__':
    unittest.main()
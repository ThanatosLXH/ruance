#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 21:58
# @Author  : LXH
# @File    : test_baidu_news.py

import unittest,time,ddt
from selenium import webdriver
from utils.excel_read import ReadExcel

excel_path = './../data_manage/test.xlsx'
sheetName = 'data_new'
excel = ReadExcel(excel_path,sheetName)
chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
@ddt.ddt
class Test_baidu_News(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()
    def setUp(self) -> None:
        self.driver.get('http://news.baidu.com')
    def tearDown(self) -> None:
        pass
    @ddt.data(*excel.getDataFromSheet())
    def test_sou(self, data1):
        self.driver.find_element_by_id('ww').send_keys(data1)
        time.sleep(2)
        self.driver.find_element_by_id('s_btn_wr').click()
        time.sleep(2)
        self.assertEqual('百度资讯搜索_'+data1, self.driver.title)

if __name__ == '__main__':
    unittest.main()

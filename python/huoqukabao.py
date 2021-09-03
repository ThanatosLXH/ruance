#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 15:12
# @Author  : LXH
# @File    : huoqukabao.py

from selenium import webdriver
import time
import requests
import urllib3
import json
import sys

chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chrome_driver)

driver.get('https://plogin.m.jd.com/login/login')
time.sleep(1)

# cookie = driver.get_cookies()
# print(cookie)
cookie = 'pt_pin=jd_46a7c233bd988;pt_key=AAJhGIxMADDu4O_XR4bc_h8cmBa5Fb64gP5StX61kwtP7E-QrBPTdJLWezVMxnldeF6E2mdOHHI'


for cook in cookie.split(';', 1):
    driver.add_cookie({"name": cook.split("=")[0].strip(" "), "value": cook.split("=")[1].strip(";"), "domain": ".jd.com"})

driver.get('https://shopmember.m.jd.com/member/memberCloseAccount?venderId=1000000912')

# driver.find_element_by_id("mCommonMy").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/button').click()

# driver.find_element_by_xpath('//*[@id="shoplist"]/div[1]/a/div/div[1]/p').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="shop"]/div[5]/div[4]/span').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="hello"]/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span').click()


#百度API
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=jRxi3aYQHRSKGksCEsLIa0b0&client_secret=f2hWPHzYQQSjcYx8Gad4XqxrIMhTYcRC'
response = requests.get(host)
if response:
    print(response.json())

token = response.json()['access_token']


import base64

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('code.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())

time.sleep(1)
driver.find_element_by_id('code').send_keys(response.json())
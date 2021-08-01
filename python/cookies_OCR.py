#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 16:07
# @Author  : LXH
# @File    : cookies_OCR.py


# from selenium import webdriver
# import time
#
# chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
# driver=webdriver.Chrome(executable_path=chrome_driver)
#
# driver.get('https://yun.baidu.com/')
# time.sleep(2)
#
# cookie = [{'domain': '.yun.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1627114788'}, {'domain': 'yun.baidu.com', 'expiry': 1629793186, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': 'f23abb2016b347abfa3053c8a6007a5c2ff96739bf777f197177ab8777cad907'}, {'domain': '.yun.baidu.com', 'expiry': 1658650787, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1627114788'}, {'domain': 'yun.baidu.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'e1dwJ-ma_KO1TUXwKNF1ySOY'}, {'domain': 'yun.baidu.com', 'expiry': 4219114786, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1886314785, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'R4RTd3d2VzakNiT25taFZXb0VpczVXb1pEZ0U0fkRxdGFBS1BTWkR5c2hXaU5oSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHN-2AhzftgTj'}, {'domain': '.yun.baidu.com', 'expiry': 1627201187, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '15390367257313616175%3AHSTAF2XekfrxLVWUjOcqv5gtJeEFa7WQCBQU2mgeV9kqt5XPvJsygTgOvhx7XIhXUNZZMVNhUv12CROZ1D50uzKeuqtLKNuit79YJhT7teIO1MJzpmpaMfdNRjGjvgE7YmxM3AJw%2FjXS%2Fb0eg7IHE7tbT0VT6%2Bsu3w1F3sQDl37Z81l%2BOzvAFj9yggFRCkDaO6gB4KX1MEY%3D'}, {'domain': '.baidu.com', 'expiry': 1886314785, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'R4RTd3d2VzakNiT25taFZXb0VpczVXb1pEZ0U0fkRxdGFBS1BTWkR5c2hXaU5oSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHN-2AhzftgTj'}, {'domain': '.baidu.com', 'expiry': 1658650775, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'DE3EFAC66EB2500F212BED0619B11564:FG=1'}, {'domain': '.baidu.com', 'expiry': 1658650775, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'DE3EFAC66EB2500F212BED0619B11564:FG=1'}]
# for cook in cookie:
#     driver.add_cookie(cook)
#
# driver.get('https://yun.baidu.com/')

from selenium import webdriver
from PIL import Image
import time
import pytesseract

chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chrome_driver)
#截屏幕
driver.get('http://htgs.ccgp.gov.cn/GS8/contractpublish/search')
driver.maximize_window()
time.sleep(2)
driver.get_screenshot_as_file('reg.png')
#定位验证码图片
code_image = driver.find_element_by_xpath('//*[@id="codeImgDiv"]/img')
# print(code_image.location)
# print(code_image.size)
left = 758
top = 397
right = 828
bottom = 427
#截取验证码
ig = Image.open('reg.png')
jie = ig.crop((left,top,right,bottom))
jie.save('code.png')

image = Image.open('code.png')
code = pytesseract.image_to_string(image)
code1 = code.replace(' ','')
print(code1)
driver.find_element_by_id('searchSupplyName').send_keys('华为')
time.sleep(1)
driver.find_element_by_id('code').send_keys(code1)
time.sleep(3)
driver.find_element_by_id('queryBtn').click()


# import requests
#
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=jRxi3aYQHRSKGksCEsLIa0b0&client_secret=f2hWPHzYQQSjcYx8Gad4XqxrIMhTYcRC'
# response = requests.get(host)
# if response:
#     print(response.json())
#
# token = response.json()['access_token']


# import base64
#
# '''
# 通用文字识别
# '''
#
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# # 二进制方式打开图片文件
# f = open('code.png', 'rb')
# img = base64.b64encode(f.read())
#
# params = {"image":img}
# access_token = token
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())
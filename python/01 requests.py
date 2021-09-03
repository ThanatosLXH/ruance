#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 16:52
# @Author  : LXH
# @File    : 01 requests.py

import requests
import os
#
# useragent = {'user-agent': 'Mozilla/5.0'}
# # keyword = {'wd': 'python'}
# url = 'http://bpic.588ku.com/element_origin_min_pic/16/10/29/2ac8e99273bc079e40a8dc079ca11b1f.jpg'
# root = 'E://picture/'
# path = root + url.split('/')[-1]

# try:
#     r = requests.get(url, headers=useragent, params=keyword)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.url)
#
# except:
#     print('爬取失败')

# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url, headers=useragent)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("successfully")
#     else:
#         print('文件已存在')
# except:
#     print('failed')

useragent = {'user-agent': 'Mozilla/5.0'}
url = 'https://www.hao123.com/'

html = requests.get(url, headers=useragent)
cookie = html.cookies
print(cookie)
for cook in cookie:
    print(cook)
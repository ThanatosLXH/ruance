#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 14:26
# @Author  : LXH
# @File    : 02 beautifulsoup.py

import requests
from bs4 import BeautifulSoup
import bs4
useragent = {'user-agent': 'Mozilla/5.0'}

def gethtml(url):
    try:
        r = requests.get(url, headers=useragent, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def tiquxinxi(num,html):
    soup = BeautifulSoup(html, 'html.parser')
    u = soup.find('div', id='data196075').find_all('td')
    for i in range(4, (num+1)*4):
        if (i + 1) % 4 == 0 and (i + 1) % 100 != 0:
            print('{0:10}\t{1:{4}^20}\t{2:^20}\t{3:{4}^20}'.format(u[i - 3].string, u[i - 2].string, u[i - 1].string,
                                                                   u[i].string, chr(12288)))


# def printpaiming(ulist, num):
#     print('{0:10}\t{1:^10}\t{2:^10}'.format('名次', '学校名称', '综合得分'))
#     for i in range(num):
#         m = ulist[i+1]
#         print('{0:10}\t{1:^10}\t{2:^10}'.format(m[0], m[1], m[2]))


def main():
    url = 'http://www.gaosan.com/gaokao/196075.html'
    r = gethtml(url)
    # uinfo = []
    tiquxinxi(200, r)
    # printpaiming(uinfo, 100)


main()

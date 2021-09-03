#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 18:20
# @Author  : LXH
# @File    : 03 re_use.py

# import requests
# from bs4 import BeautifulSoup
# import re

#股票代码爬取
# def getHTMLText(url, code="utf-8"):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = code
#         return r.text
#     except:
#         return ""
#
# def getStockList(lst, stockURL):
#     count = 0
#     html = getHTMLText(stockURL)
#     soup = BeautifulSoup(html, 'html.parser')
#     div = soup.find('div', class_='ngbglistdiv')
#     a = div.find_all('a')
#     print(a)
#     for i in a:
#         try:
#             href = i.attrs['href']
#             lst.append(re.findall(r"\d{6}", href)[0])
#
#         except:
#             continue
#
#     for i in lst:
#         print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
# def main():
#     stock_list_url = 'https://guba.eastmoney.com/remenba.aspx?type=1'
#     stock_info_url = 'https://gupiao.baidu.com/stock/'
#     output_file = 'D:/BaiduStockInfo.txt'
#     slist=[]
#     getStockList(slist, stock_list_url)
#
# main()

#淘宝商品价格信息爬取
import requests
import re


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
           'cookie': 'cna=bv6LFRw25DUCAdrF6HExI/Yt; tracknick=ws8643; enc=By1GdYXM0L3PfvN9NYkZy%2FZoi4x9GnOSd3tId7NG9k0hdj9Mtya7%2BogT0ESFkF4qAHi8pHlppHZ46wmsO%2FEqcA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; miid=2055056644898142651; lgc=ws8643; _cc_=V32FPkk%2Fhw%3D%3D; sgcookie=E100%2FA9Sl52lTus%2B7CQ8baM5W7oi4bIGunj5%2FkHSKuKu2iKE6GGKe2aXu5JN6xs2pm9phdcdnp6pAeX7CTLtQpWVaQ%3D%3D; uc3=id2=UoTV7gbvehPoDQ%3D%3D&nk2=FOpbD6os&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCuwJCqxxMEgvPbMc%3D; uc4=nk4=0%40FmENcPvsw%2F0FhV%2Bh6JTlJWs%3D&id4=0%40UOx%2FVpY5v2U5jXqDg1kMtqMhDf3X; cookie2=1011f50a13ff0f396d397889b677115a; t=4594d564f48a2f78bac8dc39d071ee92; _tb_token_=fe35a716baf38; mt=ci=-1_0; thw=cn; xlly_s=1; _m_h5_tk=a46bd7c1d18a3a7a885139010f9dc94f_1627922680814; _m_h5_tk_enc=9f05e8886bd44c0e02054dec53382104; uc1=cookie14=Uoe2ytwMwWSDRA%3D%3D; tfstk=cMAcBjwevKWjNEBkdj1Xu69tXCGdwsNNxCRWaCBJ6r-3CRC078yEEQ0lmX6LC; isg=BGlpRCAmLJA-ASw0HNM9i5CVeBXDNl1o1F55kwte5dCP0onkU4ZtOFfAlHZk0fWg; l=eBxHWWW4qNMTq66tBOfanurza77OSIRYYuPzaNbMiOCPOb5B5HRRW6htG886C3GVh6YDR3rEQAfvBeYBqQAonxv92j-la_kmn'}



def getHTMLTEXT(url):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return '页面爬取失败'

# def getINFO(lst, text):
#     try:
#         plt = re.findall(r'\"view_price\":\"\d+\.\d{2}\"', text)
#         rlt = re.findall(r'\"raw_title\":\".*?\"', text)
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(rlt[i].split(':')[1])
#             lst.append([price, title])
#
#     except:
#         print('')


def getINFO(lst, text):
    try:
        plt = re.findall(r'shopid=\"\d+?"', text)
        # rlt = re.findall(r'\"raw_title\":\".*?\"', text)
        # for i in range(len(plt)):
        #     price = eval(plt[i].split(':')[1])
        #     title = eval(rlt[i].split(':')[1])
        #     lst.append([price, title])
        print(plt)

    except:
        print('')

# def printINFO(lst):
#     tplt = "{:^4}\t{:8}\t{:16}"
#     print(tplt.format("序号", "价格", "商品名称"))
#     count = 0
#     for g in lst:
#         count = count + 1
#         print(tplt.format(count, g[0], g[1]))

def main():
    goods = '水果'
    tb_url = 'https://s.taobao.com/search?q=' + goods
    num = 1
    infolist = []
    for i in range(num):
        try:
            fullurl = tb_url + '&s=' + str(i*44)
            html = getHTMLTEXT(fullurl)
            getINFO(infolist, html)

        except:
            continue
    printINFO(infolist)

main()

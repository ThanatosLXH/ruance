#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 16:07
# @Author  : LXH
# @File    : cookies_OCR.py


# from selenium import webdriver
# import time
# import requests
#
# chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
# driver=webdriver.Chrome(executable_path=chrome_driver)
#
# driver.get('https://yun.baidu.com/')
# time.sleep(2)
#
# # cookie = driver.get_cookies()
# # print(cookie)
# cookie = [{'domain': '.yun.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1628999961'}, {'domain': 'yun.baidu.com', 'expiry': 1631678360, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '571e328dbe7b174a684c9d9e4a92a4cfe805adc95dd1a2a3ca776d2045c63f0e'}, {'domain': 'yun.baidu.com', 'expiry': 4220999960, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1888199959, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'G8zU0x3LVJ4Q0hEVU8tLWM5bUdPa2tiNGxWaDJsYzRVOE9IdUUwenpPTVhIa0JoSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABeRGGEXkRhhb'}, {'domain': '.yun.baidu.com', 'expiry': 1660535961, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1628999961'}, {'domain': 'yun.baidu.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'zoWZk33-rSesuUEjEdqmmknI'}, {'domain': '.yun.baidu.com', 'expiry': 1629086361, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '5825705628943308539%3AHSTAF2XekfrxLVWUjOcqv5gtJeEFa7WQCBQU2mgeV9kqt5XPvJsygTgOvhx7XIhXgQw5F0IWpdV2JxoWica1vzKeuqtLKNuit79YJhT7teIO1MJzpmpaMfdNRjGjvgE7YmxM3AJw%2FjXS%2Fb0eg7IHE7tbT0VT6%2Bsu3w1F3sQDl37Z81l%2BOzvAFj9yggFRCkDaO6gB4KX1MEY%3D'}, {'domain': '.baidu.com', 'expiry': 1888199959, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'G8zU0x3LVJ4Q0hEVU8tLWM5bUdPa2tiNGxWaDJsYzRVOE9IdUUwenpPTVhIa0JoSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABeRGGEXkRhhb'}, {'domain': '.baidu.com', 'expiry': 1660535944, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '34E06C582140B3937FCB5D3C7C8AF832:FG=1'}]
# # cookie = [{PSTM=1596675450; BIDUPSID=68C12F0EA0C264D2BFB4B6ECCA4005F2; __yjs_duid=1_cda876df53e96b1e975ccb41c25b34711619332839496; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=DBBE60F95326F8F1366858AB5327772C:FG=1; BDSFRCVID=1gCOJeCmHxsFtt3HBGH0JdUXugKK0gOTHllnN3-XTKW4Dk8VJeC6EG0Ptf8g0KubCWuBogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3KB6rtKRTffjrnhPF3DfLTXP6-hnjy3bRkWInvWI8aHno_bhoi5tJX3b5gLp3RymJ4QPb5bK3hDxDl5bO4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvX5Dg3-7LqU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMyModWMT-MTryKKJwaInoOK8l-UnkbhLR5fT9yMbeKHnRhlR2B-3iV-OxDUvnyxAZyxomtfQxtNRJQR6k5-3rKq5S5-OobUPUXa59LUvLfgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLJKIBhC89DTRtMJ3X-Uvy-40XKKOLVKbCtp7keq8CDxQAjbDeXP7G0M3PWDnPhP5k2C5SVRr2y5jHhp4HjMnBtxrNb5QBM-bHfU5psIJMebAWbT8U5ecaWIriaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe6JXDN88t50Of57y0tbea-3_KRQNh4Jj5CCShGRz3Mn9WDTmWlny-hQMfKOSLxJ10fIO3J7tKMnitIv9-pnsanu2hUn6Mq5H-lD_LJjZKxtq3mkjbPbDfn02OP5PLpJhL44syP4jKMRnWnciKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCF5hC8mejtMe5PyhUjJKPRfatoh0RrjK-L_HnurDtJTXUI8LUc7hnJlbTPeapoTWIJkeM5y5tJvyT8sXnO72P7XBJALhUbcQKbUjInKy4oTjxL1Db3JKjvMtg3t3qO6blooepvoD-Jc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEK5r2SCI2JCjP; BDSFRCVID_BFESS=1gCOJeCmHxsFtt3HBGH0JdUXugKK0gOTHllnN3-XTKW4Dk8VJeC6EG0Ptf8g0KubCWuBogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3KB6rtKRTffjrnhPF3DfLTXP6-hnjy3bRkWInvWI8aHno_bhoi5tJX3b5gLp3RymJ4QPb5bK3hDxDl5bO4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvX5Dg3-7LqU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMyModWMT-MTryKKJwaInoOK8l-UnkbhLR5fT9yMbeKHnRhlR2B-3iV-OxDUvnyxAZyxomtfQxtNRJQR6k5-3rKq5S5-OobUPUXa59LUvLfgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLJKIBhC89DTRtMJ3X-Uvy-40XKKOLVKbCtp7keq8CDxQAjbDeXP7G0M3PWDnPhP5k2C5SVRr2y5jHhp4HjMnBtxrNb5QBM-bHfU5psIJMebAWbT8U5ecaWIriaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe6JXDN88t50Of57y0tbea-3_KRQNh4Jj5CCShGRz3Mn9WDTmWlny-hQMfKOSLxJ10fIO3J7tKMnitIv9-pnsanu2hUn6Mq5H-lD_LJjZKxtq3mkjbPbDfn02OP5PLpJhL44syP4jKMRnWnciKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCF5hC8mejtMe5PyhUjJKPRfatoh0RrjK-L_HnurDtJTXUI8LUc7hnJlbTPeapoTWIJkeM5y5tJvyT8sXnO72P7XBJALhUbcQKbUjInKy4oTjxL1Db3JKjvMtg3t3qO6blooepvoD-Jc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEK5r2SCI2JCjP; H_PS_PSSID=31660_26350; delPer=0; PSINO=5; BA_HECTOR=ak2h0h0h0g0100ahh51ggvrl50r; csrfToken=CBA4rJhO1OHlLep9LzKmTi0T; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1627113998,1628434941; BDUSS=1CYndHUmdiM1NCSm9Pa3hJdERTSGR2Y2F6UnVVMTZsc0dXMHMwVEhWaGtmemRoSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGTyD2Fk8g9haW; BDUSS_BFESS=1CYndHUmdiM1NCSm9Pa3hJdERTSGR2Y2F6UnVVMTZsc0dXMHMwVEhWaGtmemRoSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGTyD2Fk8g9haW; pan_login_way=1; STOKEN=eef4e5df60791e73ec29d36f672b1c0a4be2ad56be47b22a02dc35d5585536ae; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1628435046; PANPSC=16071798068849572061%3AHSTAF2XekfrxLVWUjOcqv5gtJeEFa7WQCBQU2mgeV9kqt5XPvJsygTgOvhx7XIhXjxjkQkcUzlH1%2BOwOjipAzzKeuqtLKNuit79YJhT7teIO1MJzpmpaMfdNRjGjvgE7YmxM3AJw%2FjXS%2Fb0eg7IHE7tbT0VT6%2Bsu3w1F3sQDl37Z81l%2BOzvAFj9yggFRCkDaO6gB4KX1MEY%3D}]
# #cookie = [{'domain': '.yun.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1627114788'}, {'domain': 'yun.baidu.com', 'expiry': 1629793186, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': 'f23abb2016b347abfa3053c8a6007a5c2ff96739bf777f197177ab8777cad907'}, {'domain': '.yun.baidu.com', 'expiry': 1658650787, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1627114788'}, {'domain': 'yun.baidu.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'e1dwJ-ma_KO1TUXwKNF1ySOY'}, {'domain': 'yun.baidu.com', 'expiry': 4219114786, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1886314785, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'R4RTd3d2VzakNiT25taFZXb0VpczVXb1pEZ0U0fkRxdGFBS1BTWkR5c2hXaU5oSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHN-2AhzftgTj'}, {'domain': '.yun.baidu.com', 'expiry': 1627201187, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '15390367257313616175%3AHSTAF2XekfrxLVWUjOcqv5gtJeEFa7WQCBQU2mgeV9kqt5XPvJsygTgOvhx7XIhXUNZZMVNhUv12CROZ1D50uzKeuqtLKNuit79YJhT7teIO1MJzpmpaMfdNRjGjvgE7YmxM3AJw%2FjXS%2Fb0eg7IHE7tbT0VT6%2Bsu3w1F3sQDl37Z81l%2BOzvAFj9yggFRCkDaO6gB4KX1MEY%3D'}, {'domain': '.baidu.com', 'expiry': 1886314785, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'R4RTd3d2VzakNiT25taFZXb0VpczVXb1pEZ0U0fkRxdGFBS1BTWkR5c2hXaU5oSVFBQUFBJCQAAAAAAAAAAAEAAADb~TEYbDg2NDM4OTc5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHN-2AhzftgTj'}, {'domain': '.baidu.com', 'expiry': 1658650775, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'DE3EFAC66EB2500F212BED0619B11564:FG=1'}, {'domain': '.baidu.com', 'expiry': 1658650775, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'DE3EFAC66EB2500F212BED0619B11564:FG=1'}]
# for cook in cookie:
#     driver.add_cookie(cook)
# #
# driver.get('https://yun.baidu.com/')

from selenium import webdriver
from PIL import Image
import time
import pytesseract
import requests
from io import BytesIO
import base64

chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chrome_driver)

# driver.get('http://htgs.ccgp.gov.cn/GS8/contractpublish/search')
driver.get('http://news.baidu.com')
time.sleep(2)

#拖拽页面
# driver.execute_script('scroll(0,4000)')

#利用截屏然后利用Image模块截图获取验证码图片
# driver.maximize_window()
# time.sleep(2)
# driver.get_screenshot_as_file('reg.png')
# #定位验证码图片获得验证码尺寸大小
# code_image = driver.find_element_by_xpath('//*[@id="codeImgDiv"]/img')
# # print(code_image.location)
# # print(code_image.size)
# left = 758
# top = 397
# right = 828
# bottom = 427
# #截取验证码
# ig = Image.open('code_request.png')
# jie = ig.crop((0,0,400,200))
# jie.save('code1.png')

#利用requests直接获取验证码图片
# url = driver.find_element_by_css_selector('#codeImgDiv > img').get_attribute('src')
# url = driver.find_element_by_xpath('//*[@id="codeImgDiv"]/img').get_attribute('src')
# print(url)
# r = requests.get(url)
#
# with open('code_request.png', 'wb') as f:
#     f.write(r.content)



#高精度识别
# f = open('code_request.png', 'rb')
# im = base64.b64encode(f.read())
# # im = Image.open('code.png')
# width, height = im.size
# #获取图片中的颜色，返回列表[(counts, color)...]
# color_info = im.getcolors(width*height)
# sort_color = sorted(color_info, key=lambda x: x[0], reverse=True)
# #将背景全部改为白色, 提取出字，每张图片一个字
# char_dict = {}
# for i in range(1, 6):
#     start_x = 0
#     im2 = Image.new('RGB', im.size, (255, 255, 255))
#     for x in range(im.size[0]):
#         for y in range(im.size[1]):
#             if im.getpixel((x, y)) == sort_color[i][1]:
#                 im2.putpixel((x, y), (0, 0, 0))
#                 if not start_x:
#                     start_x = x  #标记每个字符的起始位置，用于最后字符串的排序
#             else:
#                 im2.putpixel((x, y), (255, 255, 255))
#     char = pytesseract.image_to_string(im2, lang='normal',config='--psm 10')
#     char_dict[start_x] = char
# code = ''.join([item[1] for item in sorted(char_dict.items(), key=lambda i:i[0])])
# print(code)




#识别验证码

image = Image.open('code1.png')
code = pytesseract.image_to_string(image)
#去除空格
code1 = code.replace(' ','')
print(code)

# driver.find_element_by_id('searchSupplyName').send_keys('华为')
# time.sleep(1)
# driver.find_element_by_id('code').send_keys(code1)
# time.sleep(3)
# driver.find_element_by_id('queryBtn').click()

#
# import requests
#
# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=jRxi3aYQHRSKGksCEsLIa0b0&client_secret=f2hWPHzYQQSjcYx8Gad4XqxrIMhTYcRC'
# response = requests.get(host)
# if response:
#     print(response.json())
#
# token = response.json()['access_token']
#
#
# import base64
#
# '''
# 通用文字识别
# '''
#
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
# # 二进制方式打开图片文件
# f = open('code_request.png', 'rb')
# img = base64.b64encode(f.read())
#
# params = {"image":img}
# access_token = token
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())





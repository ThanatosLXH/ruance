# 微博热搜监控脚本
# 本程序基于python3.6开发,仅做技术交流
# 更新时间：2021.07.23
# 作者；lxh
import requests
from lxml import etree
from bs4 import BeautifulSoup


headlines_url = "https://s.weibo.com/top/summary"
html = requests.get(headlines_url).text
soup = BeautifulSoup(html, 'html.parser')
resou = soup.find('tbody').find_all('a')
shuzi = soup.find('tbody').find_all('span')
print(soup.td.next_sibling)
for i in range(1, 10):

    print('{0}\t{1:<}'.format(i, resou[i].string),shuzi[i-1].string)

# tree = etree.HTML(html)
# print(tree)
# result = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr') #//*[@id="pl_top_realtimehot"]/table/tbody/tr[2]/td[2]/a
# print(result)
# for post in result[1:11]:
#     headline = post.xpath('./td[2]/a/text()')[0]
#     print(headline)



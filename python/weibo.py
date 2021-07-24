# 微博热搜监控脚本
# 本程序基于python3.6开发,仅做技术交流
# 更新时间：2021.07.23
# 作者；lxh
import requests
from lxml import etree



headlines_url = "https://s.weibo.com/top/summary"
page_text = requests.get(headlines_url).text
tree = etree.HTML(page_text)
print(tree)
result = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
print(result)
for post in result[1:11]:
    headline = post.xpath('./td[2]/a/text()')[0]
    print(headline)
# # json_list = pattern.findall(html)[0]
# # json =json.loads(json_list)
# # data = "热搜排行榜"+'\n\n'+\
# #        '第1为：'+json[0]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[0]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第2为：'+json[1]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[1]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第3为：'+json[2]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[2]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第4为：'+json[3]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[3]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第5为：'+json[4]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[4]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第6为：'+json[5]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[5]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第7为：'+json[6]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[6]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第8为：'+json[7]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[7]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第9为：'+json[8]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[8]['note']+'%23&Refer=top'+'\n\n'+\
# #        '第10为：'+json[9]['note']+'\n'+'吃瓜链接：'+'https://s.weibo.com/weibo?q=%23'+json[9]['note']+'%23&Refer=top'


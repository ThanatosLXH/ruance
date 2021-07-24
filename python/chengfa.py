# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',i*j,end=' ')
#     print('\n')

#冒泡排序
# print('请输入N个数，并以空格隔开：')
# arr = input("")
# a = [int(n) for n in arr.split()]
# N=len(a)
# for i in range(1,N+1):
#     for j in range(1,N+1-i):
#         if a[j-1] < a[j]:
#             a[j-1] , a[j] = a[j] , a[j-1]
# for i in range(N):
#     print(a[i],end=',')
# print('\n')
# print(",".join(str(i)for i in a))
# a=[1,5,3,7,1,4,8,4]
# a.sort()
# print(a)

# users  = [('lxh','123'),('tdz','2345')]
# # for user in users:
# #     print(user[0])
# users.pop(0)
# print(type(users))
# print(users)

# 读取excel
# import xlrd
# xlsx_file = './config/test.xlsx'
# file = xlrd.open_workbook(xlsx_file)
# table = file.sheet_by_index(0)
# print(table.nrows,table.ncols)
# print(table.row_values(1,0,4))
# #web自动化
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# chrome_driver=r'D:\python3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
# driver=webdriver.Chrome(executable_path=chrome_driver)
# #
# driver.get('http://www.baidu.com/')
# driver.find_element_by_id('kw').send_keys('华测')
# time.sleep(1)
# driver.find_element_by_id('su').click()
# time.sleep(1)
#
# text1 = driver.find_element_by_id("content_left").text
# time.sleep(1)
# assert '华测' in text1
# driver.quit()

# 集合
# x=set(['a','b','c'])
# y=set(['a','d'])
# if x & y:
#     print('1')
#
# l1=[2,3,4]
# l2=[3,5,2]
# l11 = l1[0] + l1[1] * 10 + l1[2] * 100
# l22 = l2[0] + l2[1] * 10 + l2[2] * 100
# sum = l11 + l22
# a = sum // 100
# b = (sum // 10) % 10
# c = sum % 10
# list = [c, b, a]
# print(list)

# class ad:
#     def addTwoNumbers(self,l1:list, l2:list):
#         l11 = l1[0] + l1[1] * 10 + l1[2] * 100
#         l22 = l2[0] + l2[1] * 10 + l2[2] * 100
#         sum = l11 + l22
#         a = sum // 100
#         b = (sum // 10) % 10
#         c = sum % 10
#         list = [c, b, a]
#         print(list)
# lk=ad()
# lk.addTwoNumbers(l1=[2,3,4],l2=[1,2,3])
#
# code = '86 9p'
# # code1 = list(code)
# # print(list(code))
# # for i in code1:
# #     if i == ' ':
# #         code1.remove(i)
# # code2 = str(code1)
# # print(code2)
# print(code.replace(' ',''))

code = {'word':'[{wrd:eidnn}]'}
l1 = code['word']
j = 0
for i in l1:
    j += 1
    if i == ':':
        for j in range(j,len(l1)-2):
            print(l1[j],end='')





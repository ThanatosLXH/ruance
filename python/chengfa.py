# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',i*j,end=' ')
#     print('\n')

#冒泡排序
# print('请输入N个数，并以空格隔开：')
# arr = input("")
# a = arr.split(' ')
# N = len(a)
# for i in range(0,N-1):
#     for j in range(0,N-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
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

# code = {'word':'[{wrd:eidnn}]'}
# l1 = code['word']
# j = 0
# for i in l1:
#     j += 1
#     if i == ':':
#         for j in range(j,len(l1)-2):
#             print(l1[j],end='')

# nums = [1,2,3]
# x=0
# for i in range(1, len(nums)):
#     sumleft = 0
#     sumright = 0
#     for j in range(0, i):
#         sumleft += nums[j]
#     for m in range(i + 1, len(nums)):
#         sumright += nums[m]
#     if sumleft == sumright:
#         x=1
#         print(i)
# if x != 1:
#     print('-1')

# matrix = [
#   [1,2,3,8],
#   [4,5,6,7],
#   [7,8,9,0],
#   [8,6,7,3]
# ]
# m = len(matrix)  # m行
# n = len(matrix[0])  # n列
#
# #定义一个全为0的二维数组，才能赋值
# matrix2=[[0 for col in range(m)] for row in range(n)]
#
#
# for i in range(m):
#     for j in range(n):
#         matrix2[i][j] = matrix[m-j-1][i]
# for i in matrix2:
#     print(i)



# def wei(n):
#     N = len(str(n))
#     gaowei = n // 10 ** (N - 1)
#     yushu = n % 10 ** (N - 1)
#     nums = [gaowei]
#     for i in range(1, N):
#         gaowei = yushu // 10 ** (N - i - 1)
#         yushu = yushu % 10 ** (N - i - 1)
#         nums.append(gaowei)
#     return nums
#
# def qiuhe(nums:list):
#     sum = 0
#     for i in nums:
#         sum += i**2
#     print(sum)
#     return sum

# s = 'egg'
# print(s.index(s[2]))



# import string
#
# T = int(input())
# res = []
# for _ in range(T):
#     s = input()
#     if s[0] not in string.ascii_letters:
#         res.append('Wrong')
#         continue
#     flag = False
#     for ch in s:
#         if ch in string.digits:
#             flag = True
#         elif ch not in string.ascii_letters:
#             flag = False
#             break
#     if flag:
#         res.append('Accept')
#     else:
#         res.append("Wrong")
#
# for i in res:
#     print(i)

# num = float(input())
# zs = num // 1
# xs = num % 1
# if xs >= 0.5:
#     zs += 1
# print('{:.0%}'.format(zs))


# while True:
#     try:
#         N = int(input())
#         nums =[]
#         for i in range(N):
#             nums.append(int(input()))
#
#
#         set1=set(nums)
#         nums_new = list(set1)
#         nums_new.sort()
#         for i in nums_new:
#             print(i)
#     except:
#         break

# s = input()
# jieguo = eval(s)
# if jieguo % 1>0:
#     print(eval(s))
# elif jieguo % 1 == 0:
#     print(int(eval(s)))

# while True:
#     try:
#         str = input()
#         if len(str) <= 8:
#             print('{:0<8}'.format(str))
#         elif len(str) > 8:
#             str1 = ''
#             row = len(str) // 8
#             for i in range(8 * row):
#                 print(str[i], end='')
#                 if (i + 1) % 8 == 0:
#                     print('\n')
#             for i in range(8 * row, len(str)):
#                 str1 = str1 + str[i]
#             print('{:0<8}'.format(str1))
#
#
#     except:
#         break
#
#字典
# dict = {}
# num = int(input())
# lis = []
# for i in range(num):
#     lis.append(input())
#     zilis = lis[i].split()
#     nm = int(zilis[0])
#     if nm in dict:
#         dict[nm] = int(dict[zilis[0]]) + int(zilis[1])
#         continue
#     dict[nm] = int((zilis[1]))
# lis1 = []
# for j in sorted(dict.keys()):
#     print(j, dict[j])


# import re
# str = input().split(';')
# x = 0
# y = 0
# reg = r'[ASWD]\d{1,2}$'
# for i in range(len(str)):
#     if not re.match(reg,str[i]):
#         continue
#     if str[i][0] == 'A':
#         x -= int(str[i][1:])
#     elif str[i][0] == 'S':
#         y -= int(str[i][1:])
#     elif str[i][0] == 'W':
#         y += int(str[i][1:])
#     elif str[i][0] == 'D':
#         x += int(str[i][1:])
#
# print('{},{}'.format(x,y))

# nums = ['10', '2']
# nums = list(map(str, nums))
# nums.sort()
# print(nums)

# n = [1,2,3,5,7,2,4,6]
# for i in range(len(n)):
#     for j in range(len(n)-i):
#         if n[i] > n[i+j]:
#             n[i], n[i+j] = n[i+j], n[i]
# print(n)



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         # pre = None
#         # cur = head
#         # while cur:
#         #     temp = cur.next   # 先把原来cur.next位置存起来
#         #     cur.next = pre
#         #     pre = cur
#         #     cur = temp
#         # return pre
#         stack = []
#         cur = head
#
#         while cur:
#             stack.append(cur.val)
#             cur = cur.next
#         # for i in range(len(stack)):
#         #     lis.append(stack[len(stack)-i])
#         temp = head
#         for i in range(len(stack)):
#             temp.val = stack[len(stack)-i-1]
#             temp = temp.next
#         return head
#
# class PrintNode():
#   '''''
#   输出指定节点为起始节点的链表
#   '''
#   def print_node(self,node):
#     res_list=[]
#     while node:
#       res_list.append(str(node.val))
#       node=node.next
#     print('->'.join(res_list))
#
# if __name__ == '__main__':
#     num =[]
#     node = []
#     j= 0
#     for i in range(5):
#         num.append(int(input()))
#     while node[j]:
#         node[j] = ListNode(num[j])
#         node[j].next = node[j+1]
#         j += 1
#     printnode = PrintNode()
#     printnode.print_node(node[0])
#     j = Solution()
#     j.reverseList(node[0])
#     printnode.print_node(node[0])


# listnode = input().split(' ')
# n = len(listnode)
# delnum = listnode[-1]
# lis = listnode[1:-1]
# nm = []
#
# for i in range(len(lis)):
#     if lis[i] != delnum:
#         nm.append(lis[i])
# print(nm)
#
# students = [['john', 'A', 15], ['jane', 'B', 12], ['dave', 'B', 10]]
# li = sorted(students, key=lambda m: m[2])
# print(li)


# num = 3
# paixu = 0
# list1 = []
# for i in range(num):
#     lis=input().split(' ')
#     list1.append(lis)
# if paixu == 0:
#     list1 = sorted(list1, key = lambda s: s[1], reverse=True)
#     for i in range(len(list2)):
#         print(list2[i][0],list2[i][1])
# elif paixu == 1:
#     list1 = sorted(list1,key = lambda s: s[1])
#     for i in range(len(list2)):
#         print(list2[i][0],list2[i][1])

#
# nums = [0,0,0]
# n = len(nums)
# lis = []
# if n < 3:
#     print([])
# else:
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for m in range(j + 1, n):
#                 if nums[i] + nums[j] == -nums[m]:
#                     lis.append(sorted([nums[i], nums[j], nums[m]]))
#     if len(lis) == 1:
#         print(lis)
#     else:
#         for i in range(len(lis)):
#             for j in range(i + 1, len(lis)):
#                 if lis[i] == lis[j]:
#                     lis.pop(j)
#         print(lis)
#
# from collections import OrderedDict
# class Solution:
#     def __init__(self):
#         self.cache = OrderedDict()
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
#
#     def set(self, key, value, k):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > k:
#             self.cache.popitem(last=False)
#
#     def LRU(self, operators, k):
#         res = []
#         for opt in operators:
#             if opt[0] == 1:
#                 self.set(opt[1], opt[2], k)
#             elif opt[0] == 2:
#                 res.append(self.get(opt[1]))
#         return res

# while True:
#     try:
#         lis=[]
#         count=0
#         sum = 0
#         count1 = 0
#         while input():
#             lis.append(input())
#         for i in range(len(lis)):
#             if lis[i] < 0:
#                 count += 1
#             else:
#                 sum += lis[i]
#                 count1 += 1
#         print(count)
#         print('{:.1f}'.format(sum/count1))
#     except:
#         break

# while True:
#     try:
#         str = input()
#         dict = {}
#         for i in str:
#             if i in dict:
#                 continue
#             m = str.count(i)
#             dict[i] = m
#         k = sorted(dict.items(), key=lambda items: items[1],reverse=True)
#         n = len(k)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if k[i][1] == k[j][1]:
#                     if k[i]>k[j]:
#                         k[i], k[j] = k[j], k[i]
#         for i in k:
#             print(i[0],end='')
#     except:
#         break

# n = int(input())
# lis = map(int, input().split(' '))
# mark = int(input())
# if mark == 0:
#     lis.sort()
# else:
#     lis.sort(reversed(True))
# print(lis)


# s = input()
# n = int(input())
# lis = []
# pos1 = -1
# pos2 = -1
# abs1 = len(s)
# abs2 = len(s)
# for _ in range(n):
#     lis.append(input().split(' '))
# for i in range(n):
#     if lis[i][0] == '2':
#         index = int(lis[i][1]) - 1
#         left = index - 1
#         right = index + 1
#         if index != len(s) or index != 0:
#             while left > 0:
#                 if s[left] == s[index]:
#                     pos1 = left
#                     break
#                 left -= 1
#             while right < len(s):
#                 if s[right] == s[index]:
#                     pos2 = right
#                     break
#                 right += 1
#
#             if pos1 != -1:
#                 abs1 = index - pos1
#             elif pos2 != -1:
#                 abs2 = pos2 - index
#             elif pos1 == -1 and pos2 == -1:
#                 print('-1')
#             print(min(abs1, abs2))
#
#         elif index == len(s):
#             while left >= 0:
#                 if s[left] == s[index]:
#                     pos1 = left
#                     break
#                 left -= 1
#             if pos1 != -1:
#                 print(index-pos1)
#             else:
#                 print('-1')
#         elif index == 0:
#             while right <= len(s):
#                 if s[right] == s[index]:
#                     pos2 = right
#                     break
#                 right += 1
#             if pos2 != -1:
#                 print(pos2-index)
#             else:
#                 print('-1')
#     else:
#         s += lis[i][1]

# 全排列
# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
# res = []
#
# def backtrack(sol, nums, check):
#     if len(sol) == len(nums):
#         res.append(sol)
#         return
#
#     for i in range(len(nums)):
#         if check[i] == 1:
#             continue
#         if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
#             continue
#         check[i] = 1
#         backtrack(sol + [nums[i]], nums, check)
#         check[i] = 0
#
# check = [0 for i in range(n)]
# backtrack([], nums, check)
# print(res)
# num = []
# for i in range(10):
#     num.append(i)
# x = slice(2,-2, 1)
# print(num[x])
# print(num[2::-1])

import heapq
from memory_profiler import profile

data = list(map(int, input().split(' ')))

@profile()
def di():
    heapma = []
    for i in data:
        heapq.heappush(heapma, -i)
    for _ in range(1):
        heapq.heappop(heapma)
    return -heapma[0]

di()

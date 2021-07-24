import random
import phone
import openpyxl
import xlrd,xlwt
# sec=[3,4,5,7,8,9]
# second=random.randint(sec[0],sec[5])
# print(second)

#列表生成式
# i = [i for i in range(10) if i !=6 and i !=8 ]
# print(i)
#
# p=phone.Phone()
# result=p.find(16712526281)
# print(result)

def sum(n):
    if n<=1:
        return n
    else:
        return sum(n-1)+sum(n-2)

# for i in range(1,10):
#     sum(i)

print(sum(9))
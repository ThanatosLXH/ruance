#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 16:32
# @Author  : LXH
# @File    : excel_read.py

from openpyxl import load_workbook

class ReadExcel():
    def __init__(self, excel_path, sheetName):
        self.wb = load_workbook(excel_path)
        self.sheet = self.wb[sheetName]

    def getDataFromSheet(self):
        datalist = []
        for line in self.sheet:

            datalist.append(line[0].value)
        datalist.pop(0)
        return datalist

# if __name__ == '__main__':
#     excel_path = './../data_manage/test.xlsx'
#     sheetName = 'data_new'
#     re = ReadExcel(excel_path,sheetName)
#     print(re.getDataFromSheet())
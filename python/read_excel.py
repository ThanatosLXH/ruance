# 读取excel
# import xlrd
# xlsx_file = './config/test.xlsx'
# file = xlrd.open_workbook(xlsx_file)
# table = file.sheet_by_index(0)
# print(table.nrows,table.ncols)
# print(table.row_values(1,0,4))

# case={
#     'a':'4',
#     'b':'6',
#     'c':'7'
# }
#
# res=case['a']
# print(res)
#coding utf8
import openpyxl
wk=openpyxl.load_workbook("./test.xlsx")
sh=wk.get_sheet_by_name('Sheet1')
sh['E2']='pass'
wk.save('./test.xlsx')
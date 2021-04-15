# -*- coding: utf-8 -*-
# @Time : 2021-04-13 16:33
# @Author : bai ping
# @QQ : 376706275
import xlrd
class ExlOperation:

    def  __init__(self,path=None,sheet_name=None):
        if path==None:
            path='../../config/AutoCase.xlsx'
        else:
            path=path
        if sheet_name==None:
            sheet_name='用例参数'
        else:
            sheet_name=sheet_name
        #获取工作薄
        self.workbook = xlrd.open_workbook(path)
        #获取sheet页面
        self.sheet = self.workbook.sheet_by_name(sheet_name)


    #获取行
    def get_row(self):
        return self.sheet.nrows

    #获取列
    def get_col(self):
        return self.sheet.ncols

    #获取单元格内容
    def get_cell_value(self,nrow,ncol):
        if self.sheet.cell(nrow,ncol).ctype==0:
            return ''
        else:
            return self.sheet.cell_value(nrow,ncol)
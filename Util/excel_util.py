#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import xlrd
from xlutils.copy import copy
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
# file_path = os.path.join ( base_path + '/report/' + 'first_ddt_case.html' )
class ExcelUtil:
    def __init__(self, excel_path=None, index=None):

        if excel_path == None:
            self.excel_path = base_path + '/config/casedata.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    #获取所有数据list
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    #获取excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    #获取单元格的数据
    def get_cell_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    #写入数据
    def write_value(self, row, value):
        # 不能直接用self.data，因为该对象在初始化时就一直打开了，每次拿 的都 是已经打开的，，但保存的是另一个，所以拿数据和保存数据不一致
        # 造成写入时只写入一个，即最后一次，因为之前的都被最后一次的覆盖了，因为拿到的数据是初始化时打开的
        # read_value = self.data
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)






if __name__ == '__main__':
    excel_path = base_path + '/config/keyword.xls'
    ex = ExcelUtil(excel_path)
    # print(ex.write_value(2, 'test'))
    print(ex.get_cell_value(10, 7))

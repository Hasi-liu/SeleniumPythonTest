#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
class KeywordCase:
    def run_main(self):
        file_path = base_path + '/config/keyword.xls'
        handle_excel = ExcelUtil(file_path)
        self.action_method = ActionMethod()
        #拿到行数
        #循环行数，去执行每一行的case
        #是否执行
            #拿到执行方法
            #拿到操作值
            #拿到输入数据
            #if 是否有输入数据
                #执行方法（输入数据，操作元素）
            #if 没有输入数据
                #执行方法（操作元素）
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_cell_value(i, 3)
                if is_run == 'yes':
                    # 写入数据只有最后一个成功了，可以用下面两行试下去查找问题
                    # handle_excel.write_value(i, 'test')
                    # continue
                    method = handle_excel.get_cell_value(i, 4)
                    send_value = handle_excel.get_cell_value(i, 5)
                    handle_value = handle_excel.get_cell_value(i, 6)
                    except_result_method = handle_excel.get_cell_value(i, 7)
                    except_result = handle_excel.get_cell_value(i, 8)
                    # 预期方法和预期结果有可能为''，不是none
                    self.run_method(method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_excep_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")


    #获取预期结果值
    def get_excep_result_value(self, data):
        return data.split('=')


    def run_method(self,method, send_value='', handle_value=''):
        #action_method = ActionMethod()每次循环都会产生一个对象，造成对象不一致，所以第二次循环打开url的时候获取不到第一个对象的driver
        method_value = getattr(self.action_method, method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
            #这个不能用None，因为在excel_util里的get_cell_value做的判断，当总行数大于row时返回data,不然才返回none,所以这里永远不会返回none
        elif send_value == ''and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result



if __name__ == '__main__':
    run = KeywordCase()
    run.run_main()



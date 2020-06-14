#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
import datetime
# 当前运行文件的路径
base_path = os.getcwd()
sys.path.append(base_path)
import logging

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志
        self.consle = logging.StreamHandler()
        self.logger.addHandler(self.consle)
        # self.logger.debug("info")


        #文件名字
        # # 打印当前文件路径
        # print(os.path.abspath(__file__))
        # # 打印当前文件路径的上级路径
        # print(os.path.dirname(os.path.abspath(__file__)))
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'
        log_name = log_dir + '/' + log_file
        # print(datetime.datetime.now())---->2020-06-11 18:29:09.348354


        #文件，输出日志
        # file_path = base_path + '/log/logs/test.log'
        # file_handle = logging.FileHandler(file_path)
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s --->%(funcName)s %(lineno)d: %(levelname)s---> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)





        # self.logger.debug("test000000")
        # self.consle.close()
        # self.logger.removeFilter(self.consle)
        # self.file_handle.close()
        # self.logger.removeFilter(self.file_handle)

    def get_log(self):
        return self.logger
#如果没有打印出来日志，是因为在初始化时就执行了关闭和移除：可以直接用方法封装，可以用装饰器，可以再用一个方法封装关闭和移除操作
    def close_handle(self):
        self.consle.close()
        self.logger.removeFilter(self.consle)
        self.file_handle.close()
        self.logger.removeFilter(self.file_handle)





if __name__ == '__main__':
    log = UserLog()
    test_log = log.get_log()
    test_log.debug("测试000")
    log.close_handle()
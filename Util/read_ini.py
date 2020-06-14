#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import configparser
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)


class ReadIni():
    # def __init__(self, file_name=None, node=None):
    #     if file_name == None:
    #         file_name = base_path + '/config/LocalElement.ini'
    #     if self.node == None:
    #         self.node = 'RegisterElement'
    #     else:
    #         self.node = node
    #     self.cf = self.load_ini(file_name)


    def load_ini(self, file_name=None):
        if file_name == None:
            file_name = base_path + '/config/LocalElement.ini'
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf


    def get_value(self, key, node=None):
        cf = self.load_ini()
        if node == None:
            node = 'RegisterElement'
        data = cf.get(node, key)
        return data


if __name__ == '__main__':
    reat_ini = ReadIni()
    print(reat_ini.get_value('code_error'))

#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Util.read_ini import ReadIni
from selenium import webdriver
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

# driver = webdriver.Chrome()
class FindElement():
    def __init__(self, driver):
        self.driver = driver
        # self.driver = self.get_driver(url)

    # def get_driver(self, url):
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #     driver.maximize_window()
    #     return driver
    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('<')[0]
        value = data.split('<')[1]

        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
        except:
            return None

        # finally:
        #     self.driver.close()



if __name__ == '__main__':

    find_el = FindElement('http://test-tc.zhan.com/login')
    print(find_el.get_element('register_button'))

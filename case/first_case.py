#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# http://www.5itest.cn/register,
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from business.register_business import RegisterBusiness
from log.user_log import UserLog
from selenium import webdriver
import HTMLTestRunner
import time
import unittest
import warnings

# user_log = UserLog()
# log = user_log.get_log()
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.user_log = UserLog()
        cls.log = cls.user_log.get_log()
    @classmethod
    def tearDownClass(cls):
        cls.user_log.close_handle()


    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.log.info("This is chrome")
        self.driver.maximize_window()
        time.sleep(3)
        self.re_business = RegisterBusiness(self.driver)
        self.file_code = base_path + '/Image/test001.png'
    def tearDown(self):
	    time.sleep(3)
	    # 失败截图
	    for method_name, error in self._outcome.errors:
		    if error:
			    case_name = self._testMethodName
			    image_path = os.path.join(base_path + '/report/' + case_name+'.png')
			    self.driver.save_screenshot(image_path)

	    self.driver.close()
	    # 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    def test_login_email_error(self):
        email_error = self.re_business.login_email_error('5555@qq.com', '12', '66', self.file_code)
        self.assertFalse(email_error, '测试失败')
        '''
        if email_error == True:
            print("email_error注册成功，此条case执行失败")
        else:
            print("email_error测试成功")
        '''


    def test_login_username_error(self):
        name_error = self.re_business.login_name_error('55', '12222', '66', self.file_code)
        self.assertFalse(name_error)
        '''
        if name_error == True:
            print("name_error注册成功，此条case执行失败")
        else:
            print("name_error测试成功")
        '''


    def test_login_pwd_error(self):
        pwd_error = self.re_business.login_pwd_error('55', '12222', '666666', self.file_code)
        if pwd_error == True:
            print("pwd_error注册成功，此条case执行失败")
        else:
            print("pwd_error测试成功")


    def test_login_code_error(self):
        code_error = self.re_business.login_code_error('55', '12222', '66', self.file_code)
        if code_error == True:
            print("code_error注册成功，此条case执行失败")
        else:
            print("code_error测试成功")


    def test_login_success(self):
        self.re_business.user_base('3640', '12222', '66', '99')
        if self.re_business.register_success() == True:
            print("注册成功，此条case执行成功")
        else:
            print("注册失败")
'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_pwd_error()
    first.test_login_code_error()
    first.test_login_success()
'''

if __name__ == '__main__':
   # unittest.main()
   file_path = os.path.join(base_path + '/report/' + 'first_case.html')
   f = open(file_path, 'wb')
   suite = unittest.TestSuite()
   suite.addTest(FirstCase('test_login_email_error'))
   suite.addTest(FirstCase('test_login_username_error'))
   # unittest.TextTestRunner().run(suite)
   runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report', description='这个是我们第一次测试报告', verbosity=2)
   runner.run(suite)









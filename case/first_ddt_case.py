#!/user/bin/env python3
# -*- coding: utf-8 -*-
#邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
import ddt
import unittest
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from business.register_business import RegisterBusiness
from Util.excel_util import ExcelUtil
from selenium import webdriver
import HTMLTestRunner
import time
import unittest
import warnings
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
	@ddt.data(*data)
	def test_register_case(self, data):
		email, username, password, code, assertCode = data
		email_error = self.re_business.register_function(email, username, password, code, assertCode)
		self.assertFalse(email_error, '测试失败')


	def setUp(self):
		warnings.simplefilter('ignore', ResourceWarning)
		self.driver = webdriver.Chrome()
		self.driver.get('http://www.5itest.cn/register')
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
				image_path = os.path.join(base_path + '/report/' + case_name + '.png')
				self.driver.save_screenshot(image_path)

		# self.driver.close()
		self.driver.quit()

'''
	@ddt.data (
		['3333','Mushishi', '22', '000', 'user_email_error'],
		['3333@qq.com','11', '22', '000', 'user_email_error']
	)
	@ddt.unpack
	def test_register_case(self, email, username, password, code, assertCode):
		email_error = self.re_business.register_function(email, username, password, code, assertCode)
		self.assertFalse(email_error, '测试失败')
	'''

if __name__ == '__main__':
    unittest.main()
    # file_path = os.path.join ( base_path + '/report/' + 'first_ddt_case.html' )
    # f = open(file_path, 'wb')
    # suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first ddt report', description='这个是我们ddt测试报告',
    #                                          verbosity=2)
    # runner.run(suite)

#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
import unittest
class FirstCase01(unittest.TestCase):
    #执行装饰器下面的函数之前先执行装饰器里的函数
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls) :
        print("所有case执行之后的后置")

    def setUp(self):
        print("这是case的前置条件")
    def tearDown(self):
        print("这是case的后置条件")
    def test_first01(self):
        print("这是第一条case")
    @unittest.skip("不执行第二条")
    def test_first02(self):
        print("这是第二条case")

    def test_first03(self):
        print("这是第三条case")




if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    #执行顺序：1.命名有关2.添加顺序有关
    suite.addTest(FirstCase01('test_first03'))
    suite.addTest(FirstCase01('test_first02'))
    unittest.TextTestRunner().run(suite)


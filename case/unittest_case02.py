#!/user/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
import unittest
class FirstCase02(unittest.TestCase):
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
    def test_first001(self):
        print("这是第00一条case")
    @unittest.skip("不执行第00二条")
    def test_first002(self):
        print("这是第00二条case")

    def test_first003(self):
        print("这是第00三条case")




if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    #执行顺序：1.命名有关2.添加顺序有关
    suite.addTest(FirstCase02('test_first03'))
    suite.addTest(FirstCase02('test_first02'))
    unittest.TextTestRunner().run(suite)


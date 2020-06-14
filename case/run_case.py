#!/user/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
class RunCase(unittest.TestCase):
	def test_case01(self):
		# case_path = base_path + '/case/'
		case_path = os.path.join(base_path, 'case')
		suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
		unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
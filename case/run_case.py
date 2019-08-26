#coding=utf-8
#运行所有的case,程序的主入口,大批量运行case 的方法   直接运行一个文件即可。
import unittest
import os

class RunCase(unittest.TestCase):

	def test_case01(self):
		case_path = os.path.join(os.getcwd())
		suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
		unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
	unittest.main()
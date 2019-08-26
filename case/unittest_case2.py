#coding=utf-8
import unittest
class FirstCase2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print('case类执行前的前置条件')
	@classmethod
	def tearDownClass(cls):
		print('case类执行后的后置条件')
	def setUp(self):
		print('这是case的前置条件')

	def tearDown(self):
		print('这是case的后置条件')

	def test_first2_01(self):
		print('这是第22一条case')
	@unittest.skip('跳过执行此条case')
	def test_first2_02(self):
		print('这是第22二条case')

	def test_first2_03(self):
		print('这是第22三条case')

	def test_first2_04(self):
		print('这是第22四条case')


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(FirstCase2('test_first2_01'))
	suite.addTest(FirstCase2('test_first2_02'))
	suite.addTest(FirstCase2('test_first2_03'))
	suite.addTest(FirstCase2('test_first2_04'))
	unittest.TextTestRunner().run(suite)
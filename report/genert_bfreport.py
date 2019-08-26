#coding=utf-8
# 这是生成beautifulreport测试报告的模板
import unittest,os
from BeautifulReport import BeautifulReport
from case.first_case import FirstCase

#用例存放位置
test_case_path =r'D:\PycharmProjects\ImoockSelenium\case\first_case.py'
#生成报告的测试位置
report_dir = os.getcwd()

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(FirstCase('test_register_email_error'))
	suite.addTest(FirstCase('test_register_password_error'))
	suite.addTest(FirstCase('test_register_repeat_error'))
	runner = BeautifulReport(suite).report(filename='第一次测试报告',description='first report',report_dir=report_dir)
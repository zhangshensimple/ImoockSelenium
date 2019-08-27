#coding=utf-8

#设计case  对页面进行用例设计
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest,time
import HTMLTestRunner
from BeautifulReport import BeautifulReport
import os,sys
class FirstCase(unittest.TestCase):

	# def setUpClass(cls):
	# 	cls.driver = webdriver.Chrome()
	# 	cls.driver.get('https://sso.ifanr.com/register/')
	# 	cls.driver.maximize_window()
	# 	cls.login = RegisterBusiness(cls.driver)


	def setUp(self):

		self.driver = webdriver.Chrome()
		self.driver.get('https://sso.ifanr.com/register/')
		self.driver.maximize_window()
		self.login = RegisterBusiness(self.driver)


	def tearDown(self): # 在这个过程中解决截图操作
		time.sleep(2)
		for method_name,error in self._outcome.errors:
			if error:
				case_name = self._testMethodName
				file_name = os.path.join(os.getcwd()+'/image/'+case_name+'.png')
				self.driver.save_screenshot(file_name)
		# print(self._outcome)
		# file_name = r'D:\PycharmProjects\ImoockSelenium\Image' + 'case_name' + '.png'
		# self.driver.save_screenshot(file_name)
		# self.driver.close()

	# def tearDownClass(cls):
	# 	cls.driver.close()

	def test_register_email_error(self):#一目了然的命名 测试登录时  邮箱错误
		email_error = self.login.register_email_error('youxiangerror','34','111aaa','111aaa')
		self.assertIs(email_error,'注册成功，第一条case结果为失败,输入的邮箱为正确格式的邮箱')
		# self.assertFalse(email_error,'第一条case结果为通过，输入邮箱格式为错误，邮箱校验通过。')
		# if email_error == True:  #获取不到错误信息  就是邮箱格式为正确的
		# 	print('注册成功，第一条case结果为失败,输入的邮箱为正确格式的邮箱')
		# else:
		# 	print('注册失败。第一条case结果为通过，输入邮箱格式为错误，邮箱校验通过。')

	def test_register_password_error(self):
		password_error = self.login.register_password_error('password@126.com','password','111aaa','111')
		self.assertFalse(password_error,'case执行了')
		# if password_error == True:#获取不到密码错误元素。2次密码相同
		# 	print('注册成功，第二条case失败，2次输入密码相同')
		# else:
		# 	print('注册失败，第二条case结果为通过，输入的2次密码不一致')
	def test_register_repeat_error(self):
		repeat_error = self.login.register_repeat_error('success4@126.com','mima','111aaa','111aaa')
		self.assertFalse(repeat_error,'case执行了')

		# if repeat_error == True:#获取不到重复邮箱的错误。该邮箱未被注册
		# 	print('注册成功，第三条case失败，该邮箱未被注册')
		# else:
		# 	print('注册失败，第三条case结果为通过，该邮箱已经被注册')


	# def test_register_success(self):#测试登录成功
	# 	register_button = self.login.use_base('success5@126.com','111aaa','111aaa','111aaa')
	#
	# 	if register_button == True:
	# 		print('注册失败')
	# 	else:
	# 		print('注册成功')



# def main():
# 	first = FirstCase()
# 	first.test_register_email_error()
# 	first.test_register_password_error()
# 	first.test_register_repeat_error()
# 	# first.test_register_success()
if __name__ == '__main__':
	# file_path = os.path.join(os.getcwd() + 'report'+'first_case_report.html')
	file_path = r'D:\PycharmProjects\ImoockSelenium\report\first_case_report.html'
	f = open(file_path,'wb')
	suite = unittest.TestSuite()
	suite.addTest(FirstCase('test_register_email_error'))
	suite.addTest(FirstCase('test_register_password_error'))
	suite.addTest(FirstCase('test_register_repeat_error'))
	runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='第一次测试报告',description='first report')
	runner.run(suite)
	# runner = BeautifulReport(suite)
	# runner.report(filename='第一次测试报告',description='first report',report_dir=file_path)







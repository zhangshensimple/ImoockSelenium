#coding=utf-8

#设计case  对页面进行用例设计
from business.register_business import RegisterBusiness
from selenium import webdriver
class FirstCase(object):
	def __init__(self):
		driver = webdriver.Chrome()
		driver.get('https://sso.ifanr.com/register/')
		driver.maximize_window()
		self.login = RegisterBusiness(driver)

	def test_register_email_error(self):#一目了然的命名 测试登录时  邮箱错误
		email_error = self.login.register_email_error('34','34','111aaa','111aaa')
		if email_error == True:
			print('注册成功，case失败')
		else:
			print('第一条case成功，邮箱格式错误。')

	def test_register_password_error(self):
		password_error = self.login.register_password_error('mail@126.com','mima','111aaa','111')
		if password_error == True:
			print('注册成功，case失败')
		else:
			print('第二天case成功，2次密码不一致')
	def test_register_repeat_error(self):
		repeat_error = self.login.register_repeat_error('mail@126.com','mima','111aaa','111')
		if repeat_error == True:
			print('注册成功，case失败')
		else:
			print('注册失败，该邮箱已经被注册')

	#
	# def test_register_success(self):#测试登录成功
	# 	success = self.login.use_base('aaan11112323asd@126.com','111aaa','111aaa','111aaa')
	# 	if self.login.register_success() == True:
	# 		print('注册成功')



def main():
	first = FirstCase()
	first.test_register_email_error()
	first.test_register_password_error()
	first.test_register_repeat_error()
	# first.test_register_success()
if __name__ == '__main__':
	main()



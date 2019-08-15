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

	def test_login_email_error(self):#一目了然的命名 测试登录时  邮箱错误
		email_error = self.login.register_email_error('34','34','111aaa','111aaa')
		if email_error == True:
			print('注册成功，case失败')


	def test_login_success(self):#测试登录成功
		success = self.login.use_base('111123asd@126.com','111aaa','111aaa','111aaa')
		if self.login.register_success() == True:
			print('注册成功')



def main():
	first = FirstCase()
	first.test_login_email_error()
	first.test_login_success()
if __name__ == '__main__':
	main()



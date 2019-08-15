#配置文件的信息 存储定位信息  将整个注册流程进行模块化讲解
#coding=utf-8
#直接调用find_element中的方法获取 定位信息
from selenium import webdriver
import time,random
from base.find_element import FindElement


class RegisterFunction(object):
	def __init__(self,url,i):#构造函数
		self.driver = self.get_driver(url,i) #传入url
	#获取driver 并打开url
	def get_driver(self,url,i):
		if i == 1:
			driver = webdriver.Chrome()
		elif i == 2:
			driver = webdriver.Firefox()
		else:
			driver = webdriver.edge()

		driver.get(url)
		driver.maximize_window()
		return driver
	# 输入用户信息 需要把find_element中的信息拿进来
	def send_user_info(self,key,data):
		#element.send_keys
		self.get_user_element(key).send_keys(data)
	# 定位用户信息，获取element  用户的element 来源就是find_element中的方法来的 。把find_element 进行实例化
	def get_user_element(self,key):
		find_element = FindElement(self.driver) # 获取到的element要通过find_element中的get_element 函数
		user_element = find_element.get_element(key)
		return user_element              # 获取到user_element后 后 随便传哪一个 都可以得到
	def get_range_user(self):
		user_info = ''.join(random.sample('1234567890abcdef',6))
		return user_info

	def main(self):
		user = self.get_range_user()
		user_email = user + '@163.com'
		self.send_user_info('user_email',user_email)
		self.send_user_info('user_nick', user_email)
		self.send_user_info('passwd1', '111aaa')
		self.send_user_info('passwd2', '111aa')
		# self.get_user_element('checkbox').click
		self.get_user_element('check').click()
		self.get_user_element('agreebutton').click()
		self.get_user_element('register').click()
		error = self.get_user_element('error_info')
		if error == None:
			print('注册成功')
		else:
			self.driver.save_screenshot('D:/PycharmProjects/ImoockSelenium/Image/errorimg.png')

		time.sleep(3)
		self.driver.close()
if __name__ == '__main__':
	for i in range(3):
		register_function = RegisterFunction('https://sso.ifanr.com/register/')
		register_function.main()




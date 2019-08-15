#coding=utf-8
#page类 定义页面的元素。 给handle层提供元素的操作方法，去拿元素
from base.find_element import FindElement
class RegisterPage(object):
	def __init__(self,driver):
		self.fd = FindElement(driver)
	#获取邮箱元素
	def get_email_element(self):
		return self.fd.get_element('user_email')
	#获取昵称元素
	def get_user_nick_element(self):
		return self.fd.get_element('user_nick')
	#获取密码元素
	def get_passwd1_element(self):
		return self.fd.get_element('passwd1')
	#获取确认密码元素
	def get_passwd2_element(self):
		return self.fd.get_element('passwd2')
	#获取协议元素
	def get_check_element(self):
		return self.fd.get_element('check')
	#获取同意按钮元素
	def get_agreebutton_element(self):
		return self.fd.get_element('agreebutton')
	#获取注册按钮元素
	def get_register_element(self):
		return self.fd.get_element('register')
	#获取错误信息元素
	def get_error_info_element(self):
		return self.fd.get_element('error_info')
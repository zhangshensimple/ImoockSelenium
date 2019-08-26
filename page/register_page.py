#coding=utf-8
#page类 定义页面的元素。 给handle层提供元素的操作方法，去拿元素
from base.find_element import FindElement
class RegisterPage(object):
	def __init__(self,driver):
		self.fd = FindElement(driver)
	#获取邮箱元素
	def get_email_element(self):
		return self.fd.get_element('user_email') #配置文件中的定位方法 索引 user_email
	#获取昵称元素
	def get_user_name_element(self):
		return self.fd.get_element('user_name')
	#获取密码元素
	def get_password1_element(self):
		return self.fd.get_element('password1')
	#获取确认密码元素
	def get_password2_element(self):
		return self.fd.get_element('password2')
	#获取协议元素
	def get_checkbox_element(self):
		return self.fd.get_element('checkbox')
	#获取同意按钮元素
	def get_agreebutton_element(self):
		return self.fd.get_element('agreebutton')
	#获取注册按钮元素
	def get_register_element(self):
		return self.fd.get_element('register')
	#获取邮箱错误信息元素
	def get_email_error_info_element(self):
		return self.fd.get_element('email_error_info')
	#获取密码输入不一致错误信息元素
	def get_password_error_info_element(self):
		return self.fd.get_element('password_error_info')
	#获取重复注册邮箱错误信息
	def get_repaet_error_info_element(self):
		return self.fd.get_element('repeat_error_info')

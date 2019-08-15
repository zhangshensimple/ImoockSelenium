#coding=utf-8
from handle.register_handle import 	RegisterHandle
class RegisterBusiness(object):
	def __init__(self,driver):
		self.register_h = RegisterHandle(driver)
	#输入注册信息操作
	def use_base(self,user_email,user_name,password1,password2):
		self.register_h.send_user_email(user_email)
		self.register_h.send_username(user_name)
		self.register_h.send_password1(password1)
		self.register_h.send_password2(password2)
		self.register_h.click_check_box()
		self.register_h.click_register_button()

	def register_success(self):
		if self.register_h.get_register_text() == None:
			return True
		else:
			return False

	#执行操作  邮箱不对的情况
	def register_email_error(self,user_email,user_name,password1,password2):
		self.use_base(user_email,user_name,password1,password2)
		if self.register_h.get_error_info() == None:
			return True
		else:
			return False
	# # 执行操作 2次输入密码不对的情况
	# def register_password_error(self,user_email,user_name,password1,password2):
	# 	self.use_base(user_email,user_name,password1,password2)
	# 	if self.register_h

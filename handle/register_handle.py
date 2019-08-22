#coding=utf-8
# 对每一个页面上的元素 进行操作  ，也就是操作元素的方法 封装一层。 作为handle层。 handle层可以和page层 放在一起。
# 对page类进行操作
from page.register_page import RegisterPage
class RegisterHandle(object):
	def __init__(self,driver):
		self.driver = driver
		self.register_p = RegisterPage(self.driver)
	#输入邮箱
	def send_user_email(self,user_email):
		self.register_p.get_email_element().send_keys(user_email)  #  传的值取得是谁？配置文件里的值吗
	#输入用户名
	def send_username(self,user_name):
		self.register_p.get_user_name_element().send_keys(user_name)
	#输入密码
	def send_password1(self,password1):
		self.register_p.get_password1_element().send_keys(password1)
	#确认密码
	def send_password2(self,password2):
		self.register_p.get_password2_element().send_keys(password2)
	#获取邮箱错误信息 的显示文字
	def get_error_info(self,info,user_info):
		if info == 'email_error_info':
			text = self.register_p.get_email_error_info_element().get_attribute('value')
		else:
			text = self.register_p.get_password_error_info_element().get_attribute('value')
		return text


	#点击确认框 checkbox
	def click_check_box(self):
		self.register_p.get_checkbox_element().click()
		self.register_p.get_agreebutton_element().click()
	#点击注册按钮
	def click_register_button(self):
		self.register_p.get_register_element().click()
	#获取注册按钮的文字
	def get_register_text(self):
		return self.register_p.get_register_element().text

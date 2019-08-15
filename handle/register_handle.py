#coding=utf-8
# 对每一个页面上的元素 进行操作  ，也就是操作元素的方法 封装一层。 作为handle层。 handle层可以和page层 放在一起。
# 对page类进行操作
from page.register_page import RegisterPage
class RegisterHandle(object):
	def __init__(self,driver):
		self.driver = driver
		self.register_p = RegisterPage(self.driver)
	#输入邮箱
	def send_user_email(self,email):
		self.register_p.get_email_element().send_keys(email)  #  传的值取得是谁？配置文件里的值吗
	#输入用户名
	def send_username(self,user_nick):
		self.register_p.get_user_nick_element().send_keys(user_nick)
	#输入密码
	def send_password1(self,passwd1):
		self.register_p.get_passwd1_element().send_keys(passwd1)
	#确认密码
	def send_password2(self,passwd2):
		self.register_p.get_passwd2_element().send_keys(passwd2)
	#获取错误信息 的显示文字
	def get_error_info(self):
		self.register_p.get_error_info_element().text()

	#点击确认框 checkbox
	def click_check_box(self):
		self.register_p.get_check_element().click()
		self.register_p.get_agreebutton_element().click()
	#点击注册按钮
	def click_register_button(self):
		self.register_p.get_register_element().click()
	#获取注册按钮的文字
	def get_register_text(self):
		return self.register_p.get_register_element().text()

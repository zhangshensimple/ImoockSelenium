#coding = utf8
#将注册流程进行代码封装  是代码更加简洁  2-17
from selenium import webdriver
import time
import random
driver = webdriver.Chrome() #将driver对象放在全局 作为一个全局变量，后面的函数均可以调用该driver

#浏览器初始化
def driver_init():
	driver.get('https://sso.ifanr.com/register/')
	driver.maximize_window()
	time.sleep(3)

#获取element信息
def get_elementByxpath(xpath):
	xpathElement = driver.find_element_by_xpath(xpath)
	return xpathElement
def get_elementByclasssname(class_name):
	classnameElement = driver.find_element_by_class_name(class_name)
	return classnameElement
def get_elementByid(id):
	idElement =driver.find_element_by_id(id)
	return idElement
#获取随机数邮箱
def get_range_user():
	user_info = ''.join(random.sample('1234567890abcdef',6))
	return user_info

# #获取验证码图片
# def get_code_image(file_name):
# 	driver.save_screenshot(file_name)
#
# #解析图片

#运行主程序
def run_main():
	user_name_info = get_range_user()
	user_email = user_name_info + '@163.com'
	driver_init()
	get_elementByid('email').send_keys(user_email)
	get_elementByid('nick_name').send_keys(user_name_info)
	get_elementByid('password1').send_keys('111aaa')
	get_elementByid('password2').send_keys('111aaa')
	get_elementByxpath("//span[contains(text(),'我已阅读并同意《爱范儿用户协议》')]").click()
	get_elementByxpath("//button[contains(text(),'同意')]").click()
	get_elementByxpath("//button[text()='注册']").click()
	time.sleep(3)
	driver.save_screenshot('d:/SrcShotimg.png')

run_main()
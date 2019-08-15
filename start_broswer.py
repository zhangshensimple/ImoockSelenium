#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import random
from PIL import Image
import pytesseract
from ShowapiRequest import ShowapiRequest
import time
from selenium.webdriver.support.wait import WebDriverWait
# url='https://123.233.117.50/jnwt/indexPerson.jsp'
# driver=webdriver.Chrome()
# driver.get(url)
# time.sleep(15)
# # #使用title_contains 检查页面是否正确
# # print(EC.title_contains('百度'))
# # print(driver.title)
# # #使用except_contains判断元素是否可见
# # EC.visibility_of_all_elements_located()
# # EC.presence_of_element_located()
#
# #生成用户名 随机生成邮箱
# # for i in range(5):
# # 	user_email = ''.join(random.sample('1234567890ascdefg',5))+'@163.com' # 1234567890ascdefg中选取5个组成一个列表
# # 	print(user_email)
# IdName='371202199402064912'
# PassWord='zs064912xbbj'
# driver.find_element_by_xpath('//input[@name="certinum"]').send_keys(IdName)
# driver.find_element_by_xpath('//input[@name="perpwd"]').send_keys(PassWord)
# #解决图片验证码问题 方法一
# #第一步 使用pillow的image库 保存验证码图片
# driver.save_screenshot('d:/SrcShotimg.png')
# verifyImglocation = '//form/div[3]/div/span/img'
# code_element=driver.find_element_by_xpath(verifyImglocation)#定位验证码图片
# print(code_element.location)#（x=421，y=442）
# left = code_element.location['x']
# top = code_element.location['y']
# right = code_element.size['width']+left
# height = code_element.size['height']+top
# im = Image.open('d:/SrcShotimg.png')
# img = im.crop((left,top,right,height))
# img.save('d:/VerifyCode.png')
# #第二步  使用pytesseract 识别验证码  只能识别规则图片
# image = Image.open('d:/VerifyCode.png')
# VerifyCode = pytesseract.image_to_string(image)
# #解决图片验证码问题 方法二 见 read_image 文件
#
#
# # print(text)
# driver.find_element_by_xpath('//input[@name="vericode"]').send_keys(VerifyCode)
# driver.find_element_by_xpath('//*[@id="tabs-1"]/form/div[4]/div/button').click()
#
# driver.quit()


driver =webdriver.Chrome()
driver.get('https://dumall.baidu.com/login')
time.sleep(5) 
driver.find_element_by_xpath('//input[@name="userName"]').send_keys('15562576594')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('gm1234%A')
driver.find_element_by_css_selector('#TANGRAM__PSP_4__submit').click()

#driver.quit()



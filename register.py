#coding=utf-8
from selenium import webdriver
import random
import time


user_email = ''.join(random.sample('1234567890ascdefg',6))+'@163.com'  # 1234567890ascdefg中选取6个组成一个列表
print(user_email)
driver = webdriver.Chrome()
driver.get('https://sso.ifanr.com/register/')
driver.find_element_by_id('email').send_keys(user_email)
driver.find_element_by_id('nick_name').send_keys(user_email)
driver.find_element_by_id('password1').send_keys(user_email)
driver.find_element_by_id('password2').send_keys(user_email)
driver.find_element_by_class_name('checkbox').click()
driver.find_element_by_xpath("//button[text()='注册']").click()

print(driver.title)
driver.close()
driver.quit()





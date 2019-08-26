#定位所有元素 只需告诉我一个user_email 就可以得到，user_email 是以id= email 的方式来定位的
#coding=utf-8
from utool.read_localele_ini import ReadIni
class FindElement(object):
	def __init__(self,driver):
		self.driver = driver
	#根据元素名获取元素的定位方式和值
	def get_element(self,key):
		read_ini = ReadIni()
		data = read_ini.get_value(key)
		by = data.split(':')[0]
		value = data.split(':')[1]
		try:#添加容错处理
			if by == 'id':
				return self.driver.find_element_by_id(value)
			elif by == 'name':
				return  self.driver.find_element_by_name(value)
			elif by == 'class_name':
				return self.driver.find_element_by_classname(value)
			else:
				return self.driver.find_element_by_xpath(value)
		except:

				return None

#coding=utf-8
#读取配置文件中的信息  操作配置文件
#D:\PycharmProjects\ImoockSelenium\config\LocalElement.ini
import configparser

class ReadIni(object):
	def __init__(self,filename=None,node=None): #初始化方法 构造函数
		if filename == None:
			filename = 'D:/PycharmProjects/ImoockSelenium/config/LocalElement.ini'
		if node == None:
			self.node = 'registerElement'
		else:
			self.node = node
		self.cf = self.load_ini(filename)
#读取配置文件
	def load_ini(self,filename): # 加载文件
		cf = configparser.ConfigParser()
		cf.read(filename,encoding='utf-8') # 以配置文件的形式打开 filename
		return cf  #返回结果cf 对象，因为其他地方（函数）需要使用cf这个对象
#获取定位方式的值
	def get_value(self,key):
		data = self.cf.get(self.node,key)
		return data

if __name__ == '__main__':
	read_init = ReadIni()
	print(read_init.get_value('user_email'))

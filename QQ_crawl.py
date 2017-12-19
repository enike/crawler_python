# QQ_crawl.py
# to implement function to crawl information on qqzone
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def write_down(contents):#write_down the item needed to localhost
	try：
		f = open('D:\\Learn\\Python\\text.txt','w+',encoding='utf-8')
	except:
		print("failed to open D:\\Learn\\Python\\text.txt")
	return 1
	try:
		for row in contents:
			f.write(row)
	except:
		print("failed to write contents into the file")

def qqmail():
	mail_reader = csv.reader(open("D:\\360浏览器下载目录\\QQmail.csv",'r',encoding = 'utf-8'))
	QQnumbers=[]
	for row in mail_reader:
		qq = row[2].split("@")[0]
		try:
			int(qq)
			QQnumber.append(qq)
		except:
			print(qq,"is ilegal QQnumber")
	return QQnumbers
	
	
def crawl():
	QQnumbers = qqmail()
	for QQ in QQnumbers:
		url = 'http://user.qzone.qq.com/qq/311'.replace('qq',QQ)
		try:
			Start_Login(url)
		except:
			print(QQ,"is not ilegal or there is something wrong with your network")
			
			
def Start_Login(url):
	driver = webdriver.Firefox()
	driver.get(url)
	driver.switch_to.frame('login_frame')	#turn to iframe named login_frame
	
	driver.find_element_by_id('switcher_plogin').click()
	
	driver.find_element_by_id('u').clear()
	driver.find_element_by_id('u').send_keys('1433597346')
	driver.find_element_by_id('p').clear()
	driver.find_element_by_id('p').send_keys('liuningaiwhat..')

	driver.find_element_by_id('login_button').click()
	time.sleep(2)#waiting 2 secends for loading html
	driver.switch_to_default_content()#bug in selenium3.without this,not access to iframe named app_canvas_frame.
	
	
	driver.switch_to.frame('app_canvas_frame')
	
	
	contents = driver.find_elements_by_class_name('content')#position the specific element in the html
	
	
	write_down(contents)
	
if __name__ == '__main__':
        crawl()
		print('finish')

# QQ_crawl.py
# to implement function to crawl information on qqzone
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



		
def Start_Login():
	driver = webdriver.Firefox()
	driver.get('http://user.qzone.qq.com/982438516/311')

	driver.switch_to.frame('login_frame')	
	driver.find_element_by_id('switcher_plogin').click()
	
	driver.find_element_by_id('u').clear()
	driver.find_element_by_id('u').send_keys('1433597346')
	driver.find_element_by_id('p').clear()
	driver.find_element_by_id('p').send_keys('liuningaiwhat..')
	
	time.sleep(5)
	driver.find_element_by_id('login_button').click()
	time.sleep(5)
	driver.switch_to_default_content()
	driver.switch_to.frame('app_canvas_frame')
	contents = driver.find_elements_by_class_name('content')
	print(contents[1].text)

if __name__ == '__main__':
        Start_Login()

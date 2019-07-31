from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://appstage.sustainonline.com/")
time.sleep(10)
driver.find_element_by_link_text('Close').click()
username = driver.find_element_by_name("login")
password = driver.find_element_by_name("password") 
username.send_keys("gaurav+z11@treeni.com")
password.clear()
password.send_keys("Treeni@#1232")
# driver.implicitly_wait(10)
a = driver.find_element_by_xpath("//button[@class='so-btn so-btn-primary']")
# a = driver.find_element_by_class_name('so-btn-primary')
a.click()
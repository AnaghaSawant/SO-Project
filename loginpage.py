from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

# class SustainOnline
driver.get("https://appstage.sustainonline.com/")
time.sleep(5)
driver.find_element_by_link_text('Close').click()
username = driver.find_element_by_name("login")
password = driver.find_element_by_name("password") 
username.send_keys("gaurav+z11@treeni.com")
password.clear()
password.send_keys("Treeni@#1232")

login = driver.find_element_by_xpath("//button[@class='so-btn so-btn-primary']")
login.click()
time.sleep(3)
sustain_dev_goals = driver.find_elements_by_class_name('so-course-card-title')[2]
sustain_dev_goals.click()
time.sleep(3)
sub_course = driver.find_elements_by_class_name('so-course-card-small')[1]
sub_course.click()
time.sleep(3)
start_course = driver.find_element_by_xpath("//div[@class='overview-sidebar__header-wrap brand--head']")
start_course.click()

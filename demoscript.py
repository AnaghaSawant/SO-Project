from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://appstage.sustainonline.com/")
username = driver.find_element_by_id("id_login")
password = driver.find_element_by_id("id_password") 
username.send_keys("gaurav+z11@treeni.com")
password.clear()
password.send_keys("Treeni@#1232")

driver.find_element_by_name("submit").click()
# driver.find_element_by_css_selector(".so-btn-primary").click()

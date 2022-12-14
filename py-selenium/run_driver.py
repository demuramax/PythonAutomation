import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com')
driver.maximize_window()
# username = driver.find_element(By.ID, "user-name")  #ID
# username = driver.find_element(By.NAME, 'user-name') #Name
# username = driver.find_element(By.XPATH, '//*[@id="user-name"]') #full Xpath
username = driver.find_element(By.XPATH, '//input[@id="user-name"]') #ID Xpath
password = driver.find_element(By.CSS_SELECTOR, '#password') #CSS Selector
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")

username.send_keys("standard_user")
password.send_keys('secret_sauce')
button_login.click()




# time.sleep(2)
# driver.close()
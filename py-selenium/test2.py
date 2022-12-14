import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com'
# driver = webdriver.Firefox()

driver.get(base_url)
driver.maximize_window()

login = 'standard_use'
password_all = 'secret_sauce'

username = driver.find_element(By.XPATH, '//input[@id="user-name"]') #ID Xpath
password = driver.find_element(By.XPATH, '//*[@id="password"]') #CSS Selector
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')

username.send_keys(login)
print('Input login')
password.send_keys(password_all)
print('Input password')
button_login.click()
print('Click login button')

warning_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warning_text = warning_text.text
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
print('Good test')

driver.refresh()

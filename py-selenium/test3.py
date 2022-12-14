import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com'
# driver = webdriver.Firefox()

driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

username = driver.find_element(By.XPATH, '//input[@id="user-name"]') #ID Xpath
password = driver.find_element(By.XPATH, '//*[@id="password"]') #CSS Selector
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')

username.send_keys(login_standard_user)
print('Input login')

# username.send_keys(Keys.BACKSPACE * 2)
password.send_keys(password_all)
print('Input password')
password.send_keys(Keys.RETURN)
filter = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
filter.click()
print('Click filter')
time.sleep(3)
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)

# button_login.click()
# print('Click login button')
#
# warning_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
# value_warning_text = warning_text.text
# assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
# print('Good test')
#
# driver.refresh()

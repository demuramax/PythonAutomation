import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com'
# driver = webdriver.Firefox()

driver.get(base_url)
driver.maximize_window()

login = 'standard_user'
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
# text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "PRODUCTS"
# print('Good')

# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert get_url == url
# print('Good Url')

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d,%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('./screen/' + name_screenshot)

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

"""Info Product 1"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print('Select Product_1')

cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart.click()
print('Enter cart')

"""Info Cart Product_1"""
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('INFO Cart Product 1 Good')

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('INFO Cart Price Product 1 Good')

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print('Click Checkout')

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('Maxim')
print('Input First Name')

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('Demura')
print('Input Last Name')

zip = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip.send_keys('12345')
print('Input Zip')

button_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
button_continue.click()
print('Click continue')

"""Info Finish Product_1"""
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('INFO Cart Product 1 Good')

price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print('INFO Finish Price Product 1 Good')

summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_summary_price = summary_price.text
print(value_summary_price)

item_total = f'Item total: {value_finish_price_product_1}'
print(item_total)
assert value_summary_price == item_total
print('Total summary price is Good')
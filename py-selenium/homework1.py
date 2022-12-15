import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com'

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

"""Info Product T_shirt"""
t_shirt = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
value_t_shirt = t_shirt.text
print(value_t_shirt)

price_t_shirt = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
value_price_t_shirt = price_t_shirt.text
print(value_price_t_shirt)

select_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
select_t_shirt.click()
print(f'{value_t_shirt} is added to the cart')

"""Info Product Jacket"""
jacket = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
value_jacket = jacket.text
print(value_jacket)

price_jacket = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_jacket = price_jacket.text
print(value_price_jacket)

select_jacket = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
select_jacket.click()
print(f'{value_jacket} is added to the cart')

cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart.click()
print('Entered the cart')

"""Info Cart T_shirt"""
cart_t_shirt = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
value_cart_t_shirt = cart_t_shirt.text
print(value_cart_t_shirt)
assert value_t_shirt == value_cart_t_shirt
print('INFO Cart T-Shirt is Good')

price_cart_t_shirt = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_t_shirt = price_cart_t_shirt.text
print(value_cart_price_t_shirt)
assert value_price_t_shirt == value_cart_price_t_shirt
print('INFO Cart Price T-Shirt is Good')

"""Info Cart Jacket"""
cart_jacket = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
value_cart_jacket = cart_jacket.text
print(value_cart_jacket)
assert value_jacket == value_cart_jacket
print('INFO Cart Jacket is Good')

price_cart_jacket = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_jacket = price_cart_jacket.text
print(value_cart_price_jacket)
assert value_price_jacket == value_cart_price_jacket
print('INFO Cart Price Jacket is Good')

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print('Clicked on Checkout button')

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('Maxim')
print('Input First Name')

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('Demura')
print('Input Last Name')

zip = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip.send_keys('40450')
print('Input Zip')

button_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
button_continue.click()
print('Clicked on Continue button')

"""Info Finish T_shirt"""
finish_t_shirt = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
value_finish_t_shirt = finish_t_shirt.text
print(value_finish_t_shirt)
assert value_t_shirt == value_finish_t_shirt
print('INFO Cart T-shirt Good')

price_finish_t_shirt = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_t_shirt = price_finish_t_shirt.text
print(value_finish_price_t_shirt)
assert value_price_t_shirt == value_finish_price_t_shirt
print('INFO Finish Price T-shirt Good')

"""Info Finish Jacket"""
finish_jacket = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
value_finish_jacket = finish_jacket.text
print(value_finish_jacket)
assert value_jacket == value_finish_jacket
print('INFO Cart Jacket Good')

price_finish_jacket = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_finish_price_jacket = price_finish_jacket.text
print(value_finish_price_jacket)
assert value_price_jacket == value_finish_price_jacket
print('INFO Finish Price Jacket is Good')

summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_summary_price = float(summary_price.text[-5:])
print(f'Summary price is {value_summary_price}')

item_total = float(value_finish_price_t_shirt[1:]) + float(value_finish_price_jacket[1:])
print(f'Item Total is {item_total}')
assert value_summary_price == item_total
print('Total summary price is Good')
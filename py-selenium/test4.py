import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

# driver.execute_script("window.scrollTo(0, 500)")
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
action.move_to_element(red_t_shirt).perform()
time.sleep(3)
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d,%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('./screen/' + name_screenshot)


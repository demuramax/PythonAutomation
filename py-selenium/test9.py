import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/radio-button'
# driver = webdriver.Firefox()

driver.get(base_url)
driver.maximize_window()

# time.sleep(3)
# check_box = driver.find_element(By.XPATH, '//input[@value="cb1"]')
# check_box.click()
#
# time.sleep(3)
# check_box2 = driver.find_element(By.XPATH, '//input[@value="cb3"]')
# check_box2.click()

radio_btn = driver.find_element(By.XPATH, '//input[@id="yesRadio"]')
radio_btn.click()
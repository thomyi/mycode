#!/usr/bin/env python3

# python3 -m pip install selenium

# download gecko webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://dominos.com/en/")

time.sleep(2)
click_sign_in = driver.find_element_by_xpath("/html/body/header/nav[1]/div[1]/div[3]/a")
click_sign_in.click()

time.sleep(1)
driver.find_element_by_xpath(//*[@id="Email"].click()
driver.find_element_by_xpath(//*[@id="Email"]).send_keys("test@gmail.com")

time.sleep(1)
driver.find_element_by_xpath(//*[@id="Password"]).click()
driver.find_element_by_xpath(//*[@id="Password"]).send_keys("yummypizza" + Keys.RETURN)
time.sleep(3)

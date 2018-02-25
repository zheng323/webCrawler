import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

#open chrome driver
driver = webdriver.Chrome()

#go to Piazza login page
driver.get("https://piazza.com/account/login")

#login using email and password and click the login button
driver.find_element_by_id("email").send_keys("")
driver.find_element_by_id("password").send_keys("")
driver.find_elements_by_xpath("//button[@id='submit']")[0].click()

#wait for request to send before switching page
time.sleep(1)

#go to the
r = driver.get("https://piazza.com/class/jc6ho7dt2y2301?cid=246")

#use BeautifulSoup to retrive all information from the page
soup = BeautifulSoup(driver.page_source, "html.parser")


names = ['Patrick Yergler', 'Donnie Spencer', 'Gary McFall', 'Test Name']

#check for names
for i in names:
    if (len(soup.findAll(text = re.compile(i))) != 0) or \
       (len(soup.findAll(text = re.compile(i + '\s'))) != 0) or \
       (len(soup.findAll(text = i)) != 0) or \
       (len(soup.findAll(text = i + '\s')) != 0):
        print("true")
    else:
        print("false")


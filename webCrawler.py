import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://piazza.com/account/login")

driver.find_element_by_id("email").send_keys("zheng323@purdue.edu")
driver.find_element_by_id("password").send_keys("Zhengtiancai8!")
driver.find_elements_by_xpath("//button[@id='submit']")[0].click()
time.sleep(1)
re = driver.get("https://piazza.com/class/jc6ho7dt2y2301?cid=246")
soup = BeautifulSoup(driver.page_source)
test = soup.find(text="Patrick Yergler")
t = soup.find("div", attrs={'class' : 'discussion_text'})

print(test.text)





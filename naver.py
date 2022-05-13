from asyncio import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import time

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
driver.implicitly_wait(10)

u_str = " "
driver.find_element_by_xpath('//*[@id="nx_query"]').send_keys(u_str)
driver.find_element_by_xpath('//*[@id="nx_search_form"]/fieldset/button').click()

body = driver.find_element_by_css_selector('body')

for i in range(500):
    body.send_keys(Keys.PAGE_DOWN)

driver.implicitly_wait(60)

num = 1
createFolder('./'+u_str)
for i in range(1,10000):
    tmp = driver.find_element_by_xpath('//*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div['+str(i)+']')
    if (tmp.get_attribute('data-id') is None):
        continue
    tmp = driver.find_element_by_xpath('//*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div['+str(i)+']/div/div[1]/a/img')
    if (tmp.is_displayed()):
        if (not('data:image' in tmp.get_attribute('src'))):
            urllib.request.urlretrieve(tmp.get_attribute('src'), u_str+"/"+u_str+str(num)+".jpg")
            num += 1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

driver = webdriver.Chrome('/Users/kimhyunwoo/Desktop/Git/Web_Crawler/chromedriver')
driver.get("https://search.naver.com/search.naver?where=image&section=image&query=")

search_txt = input()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(search_txt) # 구글 검색창에 문자 입력
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click() # 검색
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() # 이미지로 들어감

images = driver.find_elements_by_css_selector("#imgList > div > a > img")


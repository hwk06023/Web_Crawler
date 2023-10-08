import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.chrome.options import Options

schedule_time = datetime() # input schedule time
options = Options()

options.add_experimental_option("detach", True)
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 1)

set_schedule = False

uId = ''
uPw = ''

def interval_time():
    n = datetime.now()

    print("interval start - now({}), schedule({})".format(n, schedule_time))

    interval = schedule_time - n
    interval_seconds = interval.seconds + 1

    print("inerval time - {}".format(interval_seconds))

    if (interval.days < 0):
        print("previous time can't interval")
    else:
        time.sleep(interval_seconds)

    print("interval end - {}".format(datetime.now()))


def log_in():
    try:
        login_url = "https://accounts.interpark.com/login/form"
        driver.get(login_url)
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(uId)  # ID 입력
        driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(uPw)
        driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()
    except Exception as e:
        print(e)
        print("got exception(log_in)")

def move_to_ticket_page():
    try:
        공연코드 = 00000000
        
        userSearch = f"https://tickets.interpark.com/goods/{공연코드}#"
        driver.get(userSearch)
        time.sleep(0.7)
        
        img_capture = pyautogui.locateOnScreen("reservationIcon.png")
        print(img_capture)
        pyautogui.click(img_capture)
        sleep(100)


    except Exception as e:
        print(e)
        print("got exception(move_to_ticket_page)")

if (set_schedule):
    interval_time()

log_in()
move_to_ticket_page()
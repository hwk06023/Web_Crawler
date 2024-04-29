from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

urls = {
    "KR": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "JP": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ja&gl=JP&ceid=JP%3Aja",
    "CN": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans",
    "EN": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=en-US&gl=US&ceid=US%3Aen",
}


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def fetch_entertainment_links(driver, urls):
    for country, url in urls.items():
        file_name = f"Entertainment_{country}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Entertainment News in {country}\n\n")
            driver.get(url)
            time.sleep(10)

            for i in range(1, 6):
                link_tag = driver.find_element(
                    By.CSS_SELECTOR,
                    f"i10-panel > c-wiz > c-wiz:nth-child({i}) > c-wiz > div > article > a",
                )
                if link_tag:
                    link_url = link_tag.get_attribute("href")
                    print(link_url)
                    driver.get(link_url)
                    time.sleep(4)
                    print(driver)

                    text = driver.find_element(By.TAG_NAME, "body").text
                    cleaned_text = " ".join(text.split())

                    file.write(f"{link_url}\n")
                    file.write(f"{cleaned_text}\n\n")


driver = setup_driver()
fetch_entertainment_links(driver, urls)
driver.quit()

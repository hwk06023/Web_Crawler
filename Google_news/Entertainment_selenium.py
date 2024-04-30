from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

urls = {
    "EN": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=en-US&gl=US&ceid=US%3Aen",
    "CN": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans",
    "KR": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "JP": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ja&gl=JP&ceid=JP%3Aja",
}


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def fetch_entertainment_links(country, url):
    file_name = f"Entertainment_{country}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Entertainment News in {country}\n\n")
        idx = 1
        while idx < 6:
            link_tag = None
            driver.get(url)
            time.sleep(5)
            print(country, idx)
            crawling_success = False
            try:
                link_tag = driver.find_element(
                    By.XPATH,
                    f'//*[@id="i10-panel"]/c-wiz/c-wiz[{idx}]/c-wiz/div/article/a',
                )
                crawling_success = True
            except:
                link_tag = driver.find_element(
                    By.XPATH,
                    f'//*[@id="i10-panel"]/c-wiz/c-wiz[{idx}]/c-wiz/article/div[1]/div[2]/div/a',
                )
                crawling_success = True
            finally:
                if crawling_success == False:
                    continue
            if link_tag:
                link_url = link_tag.get_attribute("href")
                driver.get(link_url)
                time.sleep(6)

                text = driver.find_element(By.TAG_NAME, "body").text
                cleaned_text = " ".join(text.split())

                print(link_url)
                print(cleaned_text)

                file.write(f"{link_url}\n")
                file.write(f"{cleaned_text}\n\n")
                idx += 1


driver = setup_driver()

for country, url in urls.items():
    fetch_entertainment_links(country, url)

driver.quit()

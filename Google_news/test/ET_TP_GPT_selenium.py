from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
import time, math, os

from dotenv import load_dotenv

if not load_dotenv():
    raise KeyError
client = OpenAI()

urls = {
    "US": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=en-US&gl=US&ceid=US%3Aen",
    "CN": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans",
    "KR": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "JP": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ja&gl=JP&ceid=JP%3Aja",
}


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument( "user-agent=Mozilla/5.0 ~~ ." )
    driver = webdriver.Chrome(options=options)
    return driver


def summarize_gpt_api(post_content: str, prompt: str, max_length: int) -> str:
    summarized_text = ""
    tmp_li = []
    while len(post_content) > max_length:
        num_parts = math.ceil(len(post_content) / max_length)
        part_length = len(post_content) // num_parts
        for j in range(num_parts):
            start_index = j * part_length
            end_index = start_index + part_length
            content_part = post_content[start_index:end_index]
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content_part},
                ],
            )
            tmp_li.append(response.choices[0].message.content)
        post_content = " ".join(tmp_li)
        if len(post_content) <= max_length:
            summarized_text = post_content
            break
    else:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": post_content},
            ],
        )
        tmp_li.append(response.choices[0].message.content)
        summarized_text = " ".join(tmp_li)
    return summarized_text


def fetch_entertainment_links(country, url):
    driver = setup_driver()
    file_name = f"Summarized_ET_{country}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Entertainment News in {country}\n\n")
        idx = 1
        try_count = 0
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
                    if try_count < 10:
                        try_count += 1
                        continue
                    else:
                        print(f"Failed to crawl {country} {idx}th link")
                        break
            if link_tag:
                link_url = link_tag.get_attribute("href")
                driver.get(link_url)
                print(link_url)
                time.sleep(5)
                text = driver.find_element(By.TAG_NAME, "body").text
                time.sleep(2)
                cleaned_text = " ".join(text.split())

                summarize_system_prompt = "You are a helpful assistant. If you have any important information (schedule, location ..), please keep the information, and summarize any other information. The output language is determined by the input language."
                max_length = 5000
                summarized_text = summarize_gpt_api(
                    cleaned_text, summarize_system_prompt, max_length
                )

                print(summarized_text)

                file.write(f"{link_url}\n")
                file.write(f"{summarized_text}\n\n")
                idx += 1
    driver.quit()


with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(fetch_entertainment_links, "US", urls["US"])
    executor.submit(fetch_entertainment_links, "CN", urls["CN"])
    executor.submit(fetch_entertainment_links, "KR", urls["KR"])
    executor.submit(fetch_entertainment_links, "JP", urls["JP"])

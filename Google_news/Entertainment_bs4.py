import requests
from bs4 import BeautifulSoup
import time

base = "https://news.google.com"
urls = {
    "KR": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "JP": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ja&gl=JP&ceid=JP%3Aja",
    "CN": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans",
    "US": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=en-US&gl=US&ceid=US%3Aen",
}


def fetch_entertainment_links(country, url):
    file_name = f"Entertainment_{country}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Entertainment News in {country}\n\n")
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        data_node = ["1;0", "1;1", "1;2", "1;3", "1;4"]
        filtered_divs = soup.find_all(
            "c-wiz",
            attrs={
                "jsrenderer": "ARwRbe",
                "data-node-index": lambda x: x in data_node,
            },
        )

        for div in filtered_divs:
            link_tag = div.find("a", class_="gPFEn")
            if link_tag:
                link_url = base + link_tag["href"][1:]
                linked_page_response = requests.get(link_url)
                linked_page_soup = BeautifulSoup(
                    linked_page_response.content.decode("utf-8", "replace"),
                    "html.parser",
                )

                text = linked_page_soup.get_text()
                cleaned_text = " ".join(text.split())
                time.sleep(10)

                file.write(f"{link_url}\n")
                file.write(f"{cleaned_text}\n\n")


for country, url in urls.items():
    fetch_entertainment_links(country, url)

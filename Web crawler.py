import requests
from bs4 import BeautifulSoup
import pandas as pd

df_gis = pd.read_csv('daum_gis.csv', encoding='euc-kr')

df_gis_url = df_gis['URL']

header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'}

for i in range(0, 10):
  page = requests.get(df_gis_url[i], headers=header)
  soup = BeautifulSoup(page.content, 'lxml')
  divs = soup.findAll("div", {"class": "article-head-title"})

  for div in divs:
    inner_text = div.text
    strings = inner_text.split("\n")
    print (strings[0])

  ps = soup.findAll('p')

  for p in ps:
    inner_text = p.text
    strings = inner_text.split("\n")
    print (strings[0])
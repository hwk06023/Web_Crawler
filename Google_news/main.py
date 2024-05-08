from concurrent.futures import ThreadPoolExecutor
from utils.crawl_utils import fetch_entertainment_links
from enum import Enum


class Country(Enum):
    US = "US"
    CN = "CN"
    KR = "KR"
    JP = "JP"


class Genre(Enum):
    ENTERTAINMENT = "Entertainment"
    SPORTS = "Sports"
    SCIENCE_TECHNOLOGY = "Science/Technology"
    BUSINESS = "Business"
    HEALTH = "Health"


def get_crawl_results() -> dict:
    genre_url_dict = {
        Genre.ENTERTAINMENT: "CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=",
        Genre.SPORTS: "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtdHZHZ0pMVWlnQVAB?hl=",
        Genre.SCIENCE_TECHNOLOGY: "CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnJieG9DUzFJb0FBUAE?hl=",
        Genre.BUSINESS: "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=",
        Genre.HEALTH: "CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtdHZLQUFQAQ?hl=",
    }
    common_url = "https://news.google.com/topics/"
    urls = {
        Country.US: common_url
        + genre_url_dict[Genre.ENTERTAINMENT]
        + "en-US&gl=US&ceid=US%3Aen",
        Country.CN: common_url
        + genre_url_dict[Genre.ENTERTAINMENT]
        + "zh-CN&gl=CN&ceid=CN%3Azh-Hans",
        Country.KR: common_url
        + genre_url_dict[Genre.ENTERTAINMENT]
        + "ko-KR&gl=KR&ceid=KR%3Ako",
        Country.JP: common_url
        + genre_url_dict[Genre.ENTERTAINMENT]
        + "ja&gl=JP&ceid=JP%3Aja",
    }
    results = {
        Country.US: dict(),
        Country.CN: dict(),
        Country.KR: dict(),
        Country.JP: dict(),
    }

    with ThreadPoolExecutor(max_workers=4) as executor:
        results[Country.US] = executor.submit(
            fetch_entertainment_links,
            Country.US.value,
            urls[Country.US],
            Genre.ENTERTAINMENT.value,
        )
        results[Country.CN] = executor.submit(
            fetch_entertainment_links,
            Country.CN.value,
            urls[Country.CN],
            Genre.ENTERTAINMENT.value,
        )
        results[Country.KR] = executor.submit(
            fetch_entertainment_links,
            Country.KR.value,
            urls[Country.KR],
            Genre.ENTERTAINMENT.value,
        )
        results[Country.JP] = executor.submit(
            fetch_entertainment_links,
            Country.JP.value,
            urls[Country.JP],
            Genre.ENTERTAINMENT.value,
        )

    result_dict = {
        Country.US.value: results[Country.US].result(),
        Country.CN.value: results[Country.CN].result(),
        Country.KR.value: results[Country.KR].result(),
        Country.JP.value: results[Country.JP].result(),
    }

    return result_dict


get_crawl_results()

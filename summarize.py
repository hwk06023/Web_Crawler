# -*- coding: utf-8 -*-
import math
import pandas as pd
from dotenv import load_dotenv

if not load_dotenv():
    raise KeyError
from openai import OpenAI

client = OpenAI()
# post_content is filtered data that has been scraped from the website.
post_content = "안녕 하하하 나는 웹사이트에서 왔어."
summarize_system_prompt = "You are a helpful assistant. If you have any important information (schedule, location ..), please keep the information, and summarize any other information. Answer to korean please."
max_length = 8192

print(len(post_content))


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
                model="gpt-4",
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


print("final", summarize_gpt_api(post_content, summarize_system_prompt, max_length))

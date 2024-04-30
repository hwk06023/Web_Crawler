# -*- coding: utf-8 -*-
import math
import pandas as pd
from dotenv import load_dotenv

if not load_dotenv():
    raise KeyError
from openai import OpenAI
import os

client = OpenAI()
# post_content = "안녕 하하하 나는 웹사이트에서 왔어."
summarize_system_prompt = "You are a helpful assistant. If you have any important information (schedule, location ..), please keep the information, and summarize any other information. The output language is determined by the input language."
max_length = 5000


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


folder_path = "Google_news/selenium"

txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
summarize_files = []
for file in txt_files:
    file_path = os.path.join(folder_path, file)

    with open(file_path, "r") as f:
        lines = f.readlines()

    selected_lines = [lines[3], lines[6], lines[9], lines[12], lines[15]]

    print("Summarized text for", file)
    summarize_lines = []
    for line in selected_lines:
        post_content = line.strip()
        summarized_line = summarize_gpt_api(
            post_content, summarize_system_prompt, max_length
        )
        summarize_lines.append(summarized_line)
        print(summarized_line)
    summarize_files.append((file, summarize_lines))


summarize_folder = "./Google_news/summarize"
if not os.path.exists(summarize_folder):
    os.makedirs(summarize_folder)

for file, summarize_lines in summarize_files:
    file_path = os.path.join(summarize_folder, file)
    with open(file_path, "w") as f:
        for i in range(5):
            f.write(str(i) + ". " + summarize_lines[i] + "\n\n")
        print("Saved", file_path)

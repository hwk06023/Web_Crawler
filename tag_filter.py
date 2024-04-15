from bs4 import BeautifulSoup
import re


def filter_tag(post_text):
    soup = BeautifulSoup(post_text, "lxml")
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.DOTALL)
    text = re.sub(r"<\?php.*?\?>", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = " ".join(chunk for chunk in chunks if chunk)

    return text


test_text = "<p>hello world</p>  \n  <script>ah ha ha ha</script>\n\n\n\n<p> !! </p><script>yes ~</script>"
print(filter_tag(test_text))

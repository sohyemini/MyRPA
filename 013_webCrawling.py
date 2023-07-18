import bs4.element
from bs4 import BeautifulSoup
import requests

# 뉴스 중에 '은행'이 들어간 뉴스 검색을 한 url
url = "https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&q=%EC%9D%80%ED%96%89"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("div", {"class": "wrap_cont"})
for link in links:
    title = link.find('a').text
    addr = link.find('a')["href"]
    print(title, ":", addr)


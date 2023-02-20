# 제목
import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230220"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())
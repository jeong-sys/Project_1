'''
아무것도 읽어오지 못함
'''
# 제목
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230220"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())
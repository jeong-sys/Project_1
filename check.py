# imax여부
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# 텔레그램 토큰
chat_token = "6140642407:AAEancz1HDU3-SwDYPDa7NmWFBuLO8_BVe0"
chat = telegram.Bot(token = chat_token)
# chat_id = '5508231825'

updater = Updater(chat_token, use_context = True)
dispatcher = updater.dispatcher

# Selenium_webdrivet 위치 지정
# 로그 숨기기
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', options = options)

# cgv접속
driver.get('http://www.cgv.co.kr/theaters/')
# Selenium : 위의 작업이 수행된 후 해당 접속 사이트 url 정보 가져오기
html = driver.page_source
# BeautifulSoup_html을 Parsing 함
soup = bs(html, 'html.parser')

# 서울
# movie_list = soup.select('div.sect-city')
# for i in movie_list:
#     print(i.select_one('ul > li.on > div > ul').text.strip()').text.strip())

# 제주    
# movie_list = soup.select('div.area')
# for i in movie_list:
#     ch = i.select_one('ul').text


movie_list = soup.select('div.sect-city')
for i in movie_list:
    ch = (i.select_one('ul').text.strip())

ch = ch.replace('CINE de CHEF', 'CGV')
ch = ch.replace('DRIVE IN', 'CGV')
ch = ch.split('CGV')

# print(ch)
# # 서울
# 1-31
# # 경기
# 32-57
# # 인천
# 13
# # 강원
# 5
# # 대전
# 24
# # 대구
# 8
# # 부산
# 17
# # 경상
# 17
# # 광주
# 24

print(len(ch))
#contents > div.sect-common > div > div.sect-city > ul > li.on > div > ul > li:nth-child(2) > a

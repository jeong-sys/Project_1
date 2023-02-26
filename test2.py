# 셀레니움

# 영화 제목만 모아서 출력
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# browser = webdriver.Chrome('../chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome('chromedriver.exe', options = options)


# 용산 아이파크몰
browser.get('http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230227')
browser.switch_to.frame('ifrm_movie_time_table')

# html = browser.page_source
# soup = bs(html, 'xml')
html = browser.page_source
soup = bs(html, 'html.parser')

imax = soup.select_one('span,imax')


# 영화 제목
title_list = soup.select('div.info-movie')
for i in title_list:
    # a 태그 찾고 그 안에 strong 태그 에서 제목만 찾고 공백 제거
    print(i.select_one('a > strong').text.strip())


# 셀레니움
from selenium import webdriver
from bs4 import BeautifulSoup as bs

browser = webdriver.Chrome('../chromedriver')

# 용산 아이파크몰
browser.get('http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230220')
browser.switch_to.frame('ifrm_movie_time_table')

html = browser.page_source
soup = bs(html, 'xml')
imax = soup.select_one('span,imax')

# 영화 제목
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())



# import selenium
# from selenium import webdriver

# URL = "http://www.cgv.co.kr/theaters/?areacode=03%2C205&theaterCode=0007&date=20230220"
# driver = webdriver.Chrome(executable_path='chromedriver')
# driver.get(url = URL)


# print(driver.current_url)


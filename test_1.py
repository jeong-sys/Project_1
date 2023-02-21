# 셀레니움
## Selenium, BeautifulSoup의 조합

# imax여부
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# Selenium_webdrivet 위치 지정
driver = webdriver.Chrome('../chromedriver')

# 용산 아이파크몰 url 접속
driver.get('http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230221')
# iframe 전환
## 상영 시간 부분만 출력하기 위함
driver.switch_to.frame("ifrm_movie_time_table")

# Selenium : 위의 작업이 수행된 후 해당 접속 사이트 url 정보 가져오기
html = driver.page_source
# BeautifulSoup_html을 Parsing 함
soup = bs(html, 'html.parser')
# imax 정보를 찾기 위해 imax 가져옴
imax = soup.select_one('span.imax')

# imax 확인
if imax:
    # imax를 가지고 있는 영화 찾기 위해 상위 부분으로 이동
    imax = imax.find_parent('div', class_='col-times')
    # 영화 제목 출력
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(title + 'IMAX 예매가 열렸습니다.')

else:
    print('IMAX 예매가 열리지 않았습니다.')
    

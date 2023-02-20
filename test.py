# imax 여부
# 셀레니움
from selenium import webdriver
from bs4 import BeautifulSoup as bs

browser = webdriver.Chrome('../chromedriver')

# 용산 아이파크몰
browser.get('http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230227')
browser.switch_to.frame('ifrm_movie_time_table')

html = browser.page_source
soup = bs(html, 'xml')
imax = soup.select_one('span,imax')

# imax 확인
if imax:
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(title + 'IMAX 예매가 열렸습니다.')
else:
    print('IMAX 예매가 열리지 않았습니다.')

## 오류 뜸 ! 왜 뜨는지 모르겠음 !
## 집에서 하려면 이거 가상환경 만들고 하기 ~
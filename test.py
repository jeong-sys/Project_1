'''
안되는 파일
'''
# 안됨 ! iframe 변환이 잘 되지 않았던 것 같음
# soup 부분도 변경함

# imax 여부
# 셀레니움
from selenium import webdriver
from bs4 import BeautifulSoup as bs

browser = webdriver.Chrome('../chromedriver')

# 용산 아이파크몰
browser.get('http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230301')
browser.switch_to.frame("ifrm_movie_time_table")

html = browser.page_source
soup = bs(html, 'xml')
imax = soup.select_one('span.imax')


# imax 확인
if imax:
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    if title:
        print(title + 'IMAX 예매가 열렸습니다.')
    else:
        print('IMAX 예매가 열리지 않았습니다.')

# 없을때 안뜸 
else:
    print('IMAX 예매가 열리지 않았습니다.')
    

# 오류 뜸 ! 왜 뜨는지 모르겠음 ! - 잘못 침 + imax 없을 때 오류 뜸

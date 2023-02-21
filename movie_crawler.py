'''
아무것도 읽어오지 못함
'''
# 이거 cgv 값 None으로 아무것도 못 읽어옴
## 왜 안되는지 원인파악 필요함 = url 자체 다른 거 쓰긴 하는데

# 셀레니움으로 해야할 듯

# imax 여부
import requests
from bs4 import BeautifulSoup as bs

url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230227"

html = requests.get(url)
soup = bs(html.text, 'html.parser')
# print(soup.select('div.info-movie'))
imax = soup.select_one('span.imax')

print(imax) # None 

if(imax): 
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(title + 'IMAX 예매가 열렸습니다.')

else:
    print('IMAX 예매가 아직 열리지 않았습니다.')


## cgv 홈페이지 크롤링 안됨 !
## 아무것도 안뜸

# import re

# url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20230220?"
# header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# html = requests.get(url, headers = header)
# #print(html.text)
# soup = bs(html.content)
# print(soup)
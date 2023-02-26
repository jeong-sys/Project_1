# 셀레니움
## Selenium, BeautifulSoup의 조합
### 셀레니움 + 텔레그램

# imax여부
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# 텔레그램 토큰
chat_token = "6140642407:AAEancz1HDU3-SwDYPDa7NmWFBuLO8_BVe0"
chat = telegram.Bot(token = chat_token)

# Selenium_webdrivet 위치 지정
driver = webdriver.Chrome('../chromedriver')

# 용산 아이파크몰 url 접속
driver.get('http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20230221')
# iframe 전환
## 상영 시간 부분만 출력하기 위함
driver.switch_to.frame("ifrm_movie_time_table")

def find_imax():
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
        # 텔레그램에 메시지 전송
        chat.sendMessage(chat_id = 5508231825, text = title + 'IMAX 예매가 열렸습니다.')
        # 30초마다 cgv 검사해서 imax가 열리면 스케줄러 종료
        sched.pause()

    # else:
    #     # 텔레그램에 메시지 전송
    #     chat.sendMessage(chat_id = 5508231825, text = 'IMAX 예매가 열리지 않았습니다.')

sched = BlockingScheduler()
# 30초마다 반복하여 출력
sched.add_job(find_imax, 'interval', seconds=30)
sched.start()
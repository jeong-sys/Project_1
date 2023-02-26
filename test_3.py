'''
해야하는 것
1) 개인 아이디가 아닌 모든 사용자 이용 가능
###
3) 날짜 선택 // 상영관 -> 모두 버튼 눌러서 // 코드 입력 받도록하기
###


##
고칠 것 
1) 영화관 선택에서 날짜 선택 안넘어감
2) 날짜 선택 부분(셀레니움) 개인 아이디로 사용함
3) 파일 두 개 나눠서 받아오는 걸로 바꾸기
4) 메시지 계속 오는 거 한번오면 꺼지는 걸로 바꾸기

 --> 적어도 2시 30분까지 해야 ppt 만들 수 있음
'''
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
chat_id = '5508231825'

updater = Updater(chat_token, use_context = True)
dispatcher = updater.dispatcher

# Selenium_webdrivet 위치 지정
# 로그 숨기기
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', options = options)

# 영화관 목록만 출력
# 서울, 경기, 인천, 강원, 대전/충청, 대구, 부산/울산, 경상, 광주/전라/제주
def get_command(update, context) :
    region_selected = update.callback_query
    print('1',region_selected)
    country_list = [
        [InlineKeyboardButton("서울", callback_data='s'), InlineKeyboardButton("경기", callback_data='k')],
        [InlineKeyboardButton("인천", callback_data='i'), InlineKeyboardButton("강원", callback_data='gw')],
        [InlineKeyboardButton("대구", callback_data='d'), InlineKeyboardButton("경상", callback_data='ge')],
        [InlineKeyboardButton("대전/충청", callback_data='c')],
        [InlineKeyboardButton("부산/울산", callback_data='b')],
        [InlineKeyboardButton("광주/전라/제주", callback_data='g')],
    ]

    show_markup = InlineKeyboardMarkup(country_list)
    update.message.reply_text("지역을 선택하세요", reply_markup=show_markup)

def callback_get(update, context) :
    data_selected = update.callback_query.data
    print('2', data_selected)
    if data_selected == "s":
        se_list = [
                  [InlineKeyboardButton("CGV강남", callback_data='0056'), InlineKeyboardButton("CGV강변", callback_data='0001')],
                  [InlineKeyboardButton("CGV건대입구", callback_data='0229'), InlineKeyboardButton("CGV구로", callback_data='0010')],
                  [InlineKeyboardButton("CGV대학로", callback_data='0063'), InlineKeyboardButton("CGV동대문", callback_data='0252')],
                  [InlineKeyboardButton("CGV등촌", callback_data='0230'), InlineKeyboardButton("CGV명동", callback_data='0009')],
                  [InlineKeyboardButton("CGV명동역 씨네라이브러리", callback_data='0105')],
                  [InlineKeyboardButton("CGV미아", callback_data='0057'), InlineKeyboardButton("CGV방학", callback_data='0288')],
                  [InlineKeyboardButton("CGV블광", callback_data='0030'), InlineKeyboardButton("CGV상봉", callback_data='0046')],
                  [InlineKeyboardButton("CGV성신여대입구", callback_data='0300'), InlineKeyboardButton("CGV송파", callback_data='0088')],
                  [InlineKeyboardButton("CGV수유", callback_data='0276'), InlineKeyboardButton("CGV신촌아트레온", callback_data='0150')],
                  [InlineKeyboardButton("CGV압구정", callback_data='0040'), InlineKeyboardButton("CGV여의도", callback_data='0112')],
                  [InlineKeyboardButton("CGV연남", callback_data='0292'), InlineKeyboardButton("CGV영등포", callback_data='0059')],
                  [InlineKeyboardButton("CGV왕십리", callback_data='0074'), InlineKeyboardButton("CGV용산아이파크몰", callback_data='0013')],
                  [InlineKeyboardButton("CGV중계", callback_data='0131'), InlineKeyboardButton("CGV청담씨네시티", callback_data='0107')],
                  [InlineKeyboardButton("CGV피카디리1958", callback_data='0223'), InlineKeyboardButton("CGV하계", callback_data='0164')],
                  [InlineKeyboardButton("CGV홍대", callback_data='0191')],
        ]
        show_markup = InlineKeyboardMarkup(se_list)
        context.bot.edit_message_text(text="극장을 선택해주세요.",
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      reply_markup=show_markup)
    else:
        pass

def date_choice(update, context):
    date_selected = update.callback_query.data
    print(date_selected)
    print('bye')
    # updater.chat.reply_text("날짜를 입력해주세요\n예시)20230101")
    # updates = chat.getUpdates()
    # for u in updates:
    #     print(u.message['text'])
    if date_selected != None:
        context.bot.send_message(chat_id = update.effective_chat.id, 
                                text = "날짜를 입력해주세요\n예시)20230101",
                                message_id=update.callback_query.message.message_id)


###### text로 받아오기 ! // 나누면 될듯
###### 나눠서 함수안에 있는 변수 가져오는 걸로

num_1 = '0013'
num_2 = "20230227"
url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode="+num_1+"&date="+num_2

driver.get(url)
# Selenium : 위의 작업이 수행된 후 해당 접속 사이트 url 정보 가져오기
html = driver.page_source
# BeautifulSoup_html을 Parsing 함
soup = bs(html, 'html.parser')

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
        asyncio.run(chat.sendMessage(chat_id = chat_id, text = title + 'IMAX 예매가 열렸습니다.'))
        # 30초마다 cgv 검사해서 imax가 열리면 스케줄러 종료
        sched.pause()

    else:
        # 텔레그램에 메시지 전송
        asyncio.run(chat.sendMessage(chat_id = chat_id, text = 'IMAX 예매가 열리지 않았습니다.'))

sched = BlockingScheduler()
# 30초마다 반복하여 출력
sched.add_job(find_imax, 'interval', seconds=10)
sched.start()

get_handler = CommandHandler('start', get_command)
updater.dispatcher.add_handler(get_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))

updater.start_polling(timeout=1, clean=True)
updater.idle()
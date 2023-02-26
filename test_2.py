'''
해야하는 것
1) 개인 아이디가 아닌 모든 사용자 이용 가능

###
3) 날짜 선택
###

2) 영화관 선택
4) 상영관 선택

--> 텔레그램 출력
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
# chat_id = '5508231825'

updater = Updater(chat_token, use_context = True)
dispatcher = updater.dispatcher

# Selenium_webdrivet 위치 지정
# 로그 숨기기
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', options = options)


driver.get('http://www.cgv.co.kr/theaters/')
# Selenium : 위의 작업이 수행된 후 해당 접속 사이트 url 정보 가져오기
html = driver.page_source
# BeautifulSoup_html을 Parsing 함
soup = bs(html, 'html.parser')

################
def date(update, context):
    # 날짜 입력 받기 텍스트
    update.message.reply_text("날짜를 입력해주세요\n예시)20230101")

    updates = chat.getUpdates()
    for u in updates:
        print(u.message['text'])
        
##################

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def build_button(text_list, callback_header = "") : # make button list
    button_list = []
    text_header = callback_header
    if callback_header != "" :
        text_header += ","

    # 버튼 세로로 하는거 여기 어딘가 일텐데
    for text in text_list :
        button_list.append(InlineKeyboardButton(text, callback_data=text_header + text))
        
    return button_list

# 영화관 목록만 출력
# 서울, 경기, 인천, 강원, 대전/충청, 대구, 부산/울산, 경상, 광주/전라/제주
def get_command(update, context) :
    country_list = [
        [InlineKeyboardButton("서울", callback_data='1'), InlineKeyboardButton("경기", callback_data='2')],
        [InlineKeyboardButton("인천", callback_data='3'), InlineKeyboardButton("강원", callback_data='4')],
        [InlineKeyboardButton("대구", callback_data='6'), InlineKeyboardButton("경상", callback_data='8')],
        [InlineKeyboardButton("대전/충청", callback_data='5')],
        [InlineKeyboardButton("부산/울산", callback_data='7')],
        [InlineKeyboardButton("광주/전라/제주", callback_data='9')]
    ]

    show_markup = InlineKeyboardMarkup(country_list)
    update.message.reply_text("지역을 선택하세요", reply_markup=show_markup)

def callback_get(update, context) :
    data_selected = update.callback_query.data

    theater_list = soup.select('div.sect-city')
    for i in theater_list:
        ch = (i.select_one('ul').text.strip())

    ch = ch.replace('CINE de CHEF', 'CGV')
    ch = ch.replace('DRIVE IN', 'CGV')
    ch = ch.split('CGV')

    if data_selected == "1":
        se_list = build_button(ch[1:30], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(se_list, len(se_list) - 1))
        context.bot.edit_message_text(text="극장을 선택해주세요.",
                                      chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id,
                                      reply_markup=show_markup)
            
    
get_handler = CommandHandler('start', get_command)
updater.dispatcher.add_handler(get_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))

updater.start_polling(timeout=1, clean=True)
updater.idle()


# def month_choice(update, context):
#     theater_selected = update.callback_query.data
#     print('3',theater_selected)
#     if theater_selected != None:
#         month_list = [
#                 [InlineKeyboardButton("1월", callback_data='01'), InlineKeyboardButton("2월", callback_data='02')],
#                 [InlineKeyboardButton("3월", callback_data='03'), InlineKeyboardButton("4월", callback_data='04')],
#                 [InlineKeyboardButton("5월", callback_data='05'), InlineKeyboardButton("6월", callback_data='06')],
#                 [InlineKeyboardButton("7월", callback_data='07'), InlineKeyboardButton("8월", callback_data='08')],
#                 [InlineKeyboardButton("9월", callback_data='09'), InlineKeyboardButton("10월", callback_data='10')],
#                 [InlineKeyboardButton("11월", callback_data='11'), InlineKeyboardButton("12월", callback_data='12')],
#             ]        
#         show_markup = InlineKeyboardMarkup(month_list) 
#         context.bot.edit_message_text(text="달을 선택해주세요.",
#                                         chat_id=update.callback_query.message.chat_id,
#                                         message_id=update.callback_query.message.message_id,
#                                         reply_markup=show_markup)
    
# def date_choice(update, context):
#     month_selected = update.callback_query.data
#     print(month_selected)
#     month_list = [
#         [InlineKeyboardButton("1일", callback_data='01'), InlineKeyboardButton("2일", callback_data='02')],
#         [InlineKeyboardButton("3일", callback_data='03'), InlineKeyboardButton("4일", callback_data='04')],
#         [InlineKeyboardButton("5일", callback_data='05'), InlineKeyboardButton("6일", callback_data='06')],
#         [InlineKeyboardButton("7일", callback_data='07'), InlineKeyboardButton("8일", callback_data='08')],
#         [InlineKeyboardButton("9일", callback_data='09'), InlineKeyboardButton("10일", callback_data='10')],
#         [InlineKeyboardButton("11일", callback_data='11'), InlineKeyboardButton("12일", callback_data='12')],
#         [InlineKeyboardButton("13일", callback_data='13'), InlineKeyboardButton("14일", callback_data='14')],
#         [InlineKeyboardButton("15일", callback_data='15'), InlineKeyboardButton("16일", callback_data='16')],
#         [InlineKeyboardButton("17일", callback_data='17'), InlineKeyboardButton("18일", callback_data='18')],
#         [InlineKeyboardButton("19일", callback_data='19'), InlineKeyboardButton("20일", callback_data='20')],
#         [InlineKeyboardButton("21일", callback_data='21'), InlineKeyboardButton("22일", callback_data='22')],
#         [InlineKeyboardButton("23일", callback_data='23'), InlineKeyboardButton("24일", callback_data='24')],
#         [InlineKeyboardButton("25일", callback_data='25'), InlineKeyboardButton("26일", callback_data='26')],
#         [InlineKeyboardButton("27일", callback_data='27'), InlineKeyboardButton("28일", callback_data='28')],
#         [InlineKeyboardButton("29일", callback_data='29'), InlineKeyboardButton("30일", callback_data='30')],
#         [InlineKeyboardButton("31일", callback_data='31')],
#     ]        
#     show_markup = InlineKeyboardMarkup(month_list)
#     context.bot.edit_message_text(text="날짜를 선택해주세요.",
#                                     chat_id=update.callback_query.message.chat_id,
#                                     message_id=update.callback_query.message.message_id,
#                                     reply_markup=show_markup)

import telegram
# 엄청 오류 많이 뜸.... 
'''
# 이거 버전 python-telegram-bot == 13.14
'''

# id : 5508231825

chat_token = "6140642407:AAEancz1HDU3-SwDYPDa7NmWFBuLO8_BVe0"
chat = telegram.Bot(token = chat_token)
updates = chat.getUpdates()

chat.sendMessage(chat_id = 5508231825, text = "안녕하세요")


###########
# 일정한 간격마다 지속적 실행을 통한 알리미
# 스케줄러
'''
APScheduler
1) 많은 기능을 가지고 있음
BlockingScheduler
- 하나의 프로세스를 사용할 때 사용함
'''

# 서버 구축
'''
AWS로 서버상 구축
별도 실행 없이 서버 실행으로 언제나 알림 받을 수 있도록 함
- 본인의 컴퓨터가 아닌 가상의 컴퓨터를 돌린다 ~
-> 유료 같은데 다른 서버 구축방법 있는지 보기
-> 과도한 서버 사용으로 인한 문제 발생 시 책임질 수 있음. 학습용으로 사용하기
'''

# 최종적으로 원하는 목표
'''
서울 용산아이파크몰의 imax관 예매는 빨리 사라짐
자신이 원하는 날짜를 설정한 뒤에 코드를 계속 돌리면, imax관이 생겼을 때 알림이 가도록 설정 가능함
이후 알림이 1번 발송되면 스케줄러로 30초마다 크롤링했던 것이 종료 됨
또한 따로 서버를 구축하므로써 컴퓨터를 켜놓지 않아도 휴대폰으로 알림을 받을 수 있도록 함

-> 한계 : 개인만 사용 가능함
'''

# 더 발전해서 만들 수 있는 것
'''

'''
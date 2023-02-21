# 파일 이름과 모듈 이름 동일하게 하면 안됨
import telegram

# # 봇이 비동기화 타입이라, 작동 신호 필요
# import asyncio

# async def main():
token = '6140642407:AAEancz1HDU3-SwDYPDa7NmWFBuLO8_BVe0'
bot = telegram.Bot(token = token)

for i in bot.getUpdates(): 
    print(i.mesage)

# asyncio.run(main())


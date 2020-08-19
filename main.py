import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
import telegram
import imax_crawling
import json


f = open('./secret/telegram_key.json', 'r')
j = json.loads(f.read())
f.close()
telegram_token = j.get('telegram_token')
telegram_chat_id = j.get('telegram_chat_id')
bot = telegram.Bot(token = telegram_token)
bot.sendMessage(chat_id=telegram_chat_id, text="라즈베리파이 서버가 재부팅 되었습니다.")

def job_function1():
    bot.sendMessage(chat_id=telegram_chat_id, text="라즈베리파이 서버가 잘 작동하고 있습니다.")

def job_function2():
    title = imax_crawling.job_function()
    if title:
        bot.sendMessage(chat_id=telegram_chat_id, text=title+" IMAX 예매가 열렸습니다.")
        sched.pause()        



sched = BlockingScheduler()
# sched.add_job(job_function1, 'interval', seconds=3600)
sched.add_job(job_function2, 'interval', seconds=30)
sched.start()
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
import json


f = json.loads(open('secret/telegram_key.json', 'r').read())
telegram_token = f.get('telegram_token')
telegram_chat_id = f.get('telegram_chat_id')
bot = telegram.Bot(token = telegram_token)
def job_function():
    bot.sendMessage(chat_id=telegram_chat_id, text="라즈베리파이 서버가 잘 작동하고 있습니다.")

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=60)
sched.start()
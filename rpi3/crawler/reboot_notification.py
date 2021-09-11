import telegram
import json


f = json.loads(open('secret/telegram_key.json', 'r').read())
telegram_token = f.get('telegram_token')
telegram_chat_id = f.get('telegram_chat_id')
bot = telegram.Bot(token = telegram_token)
bot.sendMessage(chat_id=telegram_chat_id, text="라즈베리파이 서버가 재부팅 되었습니다.")
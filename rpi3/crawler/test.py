import json


f = json.loads(open('secret/telegram_key.json', 'r').read())
telegram_token = f.get('telegram_token')
telegram_chat_id = f.get('telegram_chat_id')
print(telegram_token)
print(telegram_chat_id)
print(type(telegram_token))
print(type(telegram_chat_id))

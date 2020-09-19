import sys
import chatbotmodel

def proc_test(bot, update):
    bot.sendMessage('It\'s a test.')
    sound = firecracker()
    bot.sendMessage(sound)
    bot.sendMessage('Test is done.')

def proc_stop(bot, update):
    bot.sendMessage('Notification bot is not activated.')
    bot.stop()

def proc_stopstop(bot, update):
    bot.stop()

def firecracker():
    return 'Testing...'

bot = chatbotmodel.TeleBot()
bot.add_handler('testing', proc_test)
bot.add_handler('stop', proc_stop)
bot.add_handler('stopstop', proc_stopstop)
bot.start()
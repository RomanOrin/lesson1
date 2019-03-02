import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
import logging
from api_key import API_KEY
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
level=logging.INFO,
filename='bot.log'
)
def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    text='Привет, как дела?'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print (user_text)
    update.message.reply_text(user_text)

def ephem_enabler(bot, update):
    print('Вызван /planet')
    ephem_text = update.message.text
    ephem_list = ephem_text.split()
    if ephem_list[1] == 'Mars':
        date = datetime.datetime.now()
        actual_date = date.strftime('%Y/%m/%d')
        mars = ephem.Mars('{}'.format(actual_date))
        result = ephem.constellation(mars)
    else:
        result = 'some'
    update.message.reply_text(result)



def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", ephem_enabler))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
main()


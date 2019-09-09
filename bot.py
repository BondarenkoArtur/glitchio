import telebot
from os import environ
import sqlite3

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Чё, как оно?
Я короче быстренько поднял бота на публичной платформе, хз будет ли работать
Сорсы тут https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)
  
# Обработчик сообщений, содержащих документ с mime_type 'text/plain' (обычный текст)
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
    pass
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
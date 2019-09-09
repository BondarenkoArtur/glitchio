from os import environ, mkdir, path

import dataset
import jsonpickle
import telebot

BOT = telebot.TeleBot(environ['TELEGRAM_TOKEN'])
try:
    if not path.exists('.data'):
        mkdir(".data")
except OSError:
    print("Cannot create folder .data")


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    db = dataset.connect('sqlite:///.data/telebot.db')
    result = db.query('SELECT * FROM welcomes ORDER BY RANDOM() LIMIT 1')
    for row in result:
        BOT.reply_to(message, row['str'].format(environ['PROJECT_NAME']))


@BOT.message_handler(func=lambda message: True)
def store_all(message):
    db = dataset.connect('sqlite:///.data/telebot.db')
    msg_table = db['messages']
    msg_table.insert(dict(chat_id=message.chat.id, message=message.text,
                          message_id=message.message_id,
                          json=jsonpickle.encode(message)))


BOT.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'],
                                                 environ['TELEGRAM_TOKEN']))

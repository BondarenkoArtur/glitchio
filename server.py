import flask
import telebot

from bot import BOT

APP = flask.Flask(__name__)
WEBHOOK_URL_PATH = "/{}".format(BOT.token)
INDEX = open('static/index.html').read()


# Process index page
@APP.route('/')
def root():
    print('index!')
    return INDEX  # 'xd' # flask.send_from_directory('/static', 'index.html')


# Process webhook calls
@APP.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        BOT.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


if __name__ == "__main__":
    APP.run()

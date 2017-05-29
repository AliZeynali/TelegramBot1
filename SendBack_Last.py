import sys
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        print(chat_id,"  ", msg['text'])
       # bot.sendMessage(chat_id, msg['text'])

def sendMessage(message):
    content_type , chat_type, chat_id = telepot.glance(message)
    if content_type == 'text':
        bot.sendMessage(chat_id, message['text'])

token ="381283759:AAGKYVLXY758oesj5uJojgYlpTcjT_qXBCs"
bot = telepot.Bot(token)
MessageLoop(bot, sendMessage).run_as_thread()

while True:
    time.sleep(2)



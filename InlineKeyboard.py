import sys
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    # keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #                  [dict(text='Telegram URL', url='https://core.telegram.org/')],
    #                  [InlineKeyboardButton(text='Callback - show notification', callback_data='notification')],
    #                  [dict(text='Callback - show alert', callback_data='alert')],
    #                  [InlineKeyboardButton(text='Callback - edit message', callback_data='edit')],
    #                  [dict(text='Switch to using bot inline', switch_inline_query='initial query')],
    #              ])
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Press A', callback_data='a')],
        [InlineKeyboardButton(text='Press B', callback_data='b')]
    ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)


def on_callback_query(msg):
    chat_id = msg['message']['chat']['id']
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    # bot.answerCallbackQuery(query_id, text='Got it')
    string = "You pressed: " + str(query_data)
    bot.sendMessage(chat_id, string)


TOKEN = "381283759:AAGKYVLXY758oesj5uJojgYlpTcjT_qXBCs"

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print('Listening ...')

while 1:
    time.sleep(10)

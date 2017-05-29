import requests
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

last_update = "notUpdated"
data = {"دلار": "initail", "یورو": 4200, "پوند": 4500, "شاخص 1": 111, "شاخص 2": 222, "شاخص 3": 333,
        "آهن": 110, "مس": 220, "نقره": 310, "سیمان": 400, "گندم": 500, "مرکبات": 600, "تمام سکه": "initial",
        "نیم سکه": "initial", "ربع سکه": "initial"}
defCurrent = "صفحه اصلی"
current = {}


def update_data():
    global last_update
    url = "http://138.201.72.172:8000/api/V1"
    response = requests.get(url).json()
    last_update = response['updated']
    data['دلار'] = "خرید: " + str(response['dollar_buy']) + "\n" + "فروش: " + str(response['dollar_sell'])
    data['تمام سکه'] = "سکه تمام طرح جدید: " + str(response['seke_tamam_new']) + "\n" + "درصد تغییرات: " + str(
        response['seke_tamam_new_change_percent']) + \
                       "\n" + "\n" + "سکه تمام طرح قدیم: " + str(
        response['seke_tamam_old']) + "\n" + "درصد تغییرات: " + str(
        response['seke_tamam_old_change_percent'])
    data["نیم سکه"] = "نیم سکه: " + str(response['seke_nim']) + "\n" + "درصد تغییرات: " + str(
        response['seke_nim_change_percent'])
    data['ربع سکه'] = "ربع سکه: " + str(response['seke_rob']) + "\n" + "درصد تغییرات: " + str(
        response['seke_rob_change_percent'])


def nextMarkUp(nextMark, chat_id):
    markup = None
    global current
    try:
        current1 = current[chat_id]
    except KeyError:
        current.update({chat_id: "صفحه اصلی"})
        current1 = "صفحه اصلی"
    markupStart = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="قیمت ارز")], [KeyboardButton(text="شاخص بورس")], [KeyboardButton(text="معدن")]
        , [KeyboardButton(text="قیمت سکه")]
    ])
    markupMoney = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="دلار")], [KeyboardButton(text="یورو")], [KeyboardButton(text="پوند")],
        [KeyboardButton(text="بازگشت")]
    ])
    markupStock = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="شاخص 1")], [KeyboardButton(text="شاخص 2")], [KeyboardButton(text="شاخص 3")],
        [KeyboardButton(text="بازگشت")]])
    markupGoods = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="آهن")], [KeyboardButton(text="مس")], [KeyboardButton(text="نقره")],
        [KeyboardButton(text="سیمان")], [KeyboardButton(text="گندم")], [KeyboardButton(text="مرکبات")]
        , [KeyboardButton(text="بازگشت")]
    ])
    markupCoin = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="تمام سکه")], [KeyboardButton(text="نیم سکه")], [KeyboardButton(text="ربع سکه")],
        [KeyboardButton(text="بازگشت")]
    ])
    if nextMark in {"/start", "صفحه اصلی"}:
        markup = markupStart
        current[chat_id] = "صفحه اصلی"
        return markup, None
    if current1 in {"/start", "صفحه اصلی"}:
        if nextMark == "قیمت ارز":
            markup = markupMoney
            current[chat_id] = nextMark
            return markup, None
        elif nextMark == "شاخص بورس":
            markup = markupStock
            current[chat_id] = nextMark
            return markup, None
        elif nextMark == "معدن":
            markup = markupGoods
            current[chat_id] = nextMark
            return markup, None
        elif nextMark == "قیمت سکه":
            markup = markupCoin
            current[chat_id] = nextMark
            return markup, None
    if current1 == "قیمت ارز":
        if nextMark == "دلار":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "دلار"
        elif nextMark == "یورو":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "یورو"
        elif nextMark == "پوند":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "پوند"
        elif nextMark == "بازگشت":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, None

    if current1 == "شاخص بورس":
        if nextMark == "شاخص 1":
            current[chat_id] = "صفحه اصلی"
            markup = markupStart
            return markup, "شاخص 1"
        elif nextMark == "شاخص 2":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "شاخص 2"
        elif nextMark == "شاخص 3":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "شاخص 3"
        elif nextMark == "بازگشت":
            current[chat_id] = "صفحه اصلی"
            markup = markupStart
            return markup, None
    if current1 == "معدن":
        if nextMark == "آهن":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "آهن"
        elif nextMark == "مس":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "مس"
        elif nextMark == "نقره":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "نقره"
        elif nextMark == "سیمان":
            markup = markupStart
            return markup, "سیمان"
        elif nextMark == "گندم":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "گندم"
        elif nextMark == "مرکبات":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "مرکبات"
        elif nextMark == "بازگشت":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, None
    if current1 == "قیمت سکه":
        if nextMark == "تمام سکه":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "تمام سکه"
        elif nextMark == "نیم سکه":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "نیم سکه"
        elif nextMark == "ربع سکه":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, "ربع سکه"
        elif nextMark == "بازگشت":
            markup = markupStart
            current[chat_id] = "صفحه اصلی"
            return markup, None
    return None, None  # if unvalid text recieved return None
def reset_current(chat_id):
    global current
    try:
        current[chat_id] = "صفحه اصلی"
    except KeyError:
        current.update({chat_id: "صفحه اصلی"})

def on_chat_message(message):
    global current
    content_type, chat_type, chat_id = telepot.glance(message)
    print(message)
    if content_type == 'text':
        text = message['text']
        markup, stuff = nextMarkUp(text, chat_id)
        print(markup)
        print("text: " + text)
        print(10 * '*')
        if text == '/start':
            reset_current(chat_id)
            bot.sendMessage(chat_id, "سلام!", reply_markup=markup)
        elif markup == None:
            bot.sendMessage(chat_id, "Unvalid!", reply_markup=markup)
        elif markup != None:
            if stuff == None:
                bot.sendMessage(chat_id, "انتخاب کنید: ", reply_markup=markup)
            else:
                update_data()
                msg = "تاریخ به روز رسانی: " + "\n" + last_update + "\n" + "\n" + str(data[stuff])
                bot.sendMessage(chat_id, msg, reply_markup=markup)


token = "381283759:AAGKYVLXY758oesj5uJojgYlpTcjT_qXBCs"
bot = telepot.Bot(token)
bot.message_loop({'chat': on_chat_message})

while True:
    time.sleep(10)

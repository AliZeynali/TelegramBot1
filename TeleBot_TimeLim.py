import telepot
import time
import time

token = "381283759:AAGKYVLXY758oesj5uJojgYlpTcjT_qXBCs"
TelegramBot = telepot.Bot(token)
AllData = TelegramBot.getUpdates()
print(AllData)
print(10 * '*')
time.sleep(2)
index = len(AllData)
# initialTime = AllData[-1]['message']['date']
# chatID = AllData[-1]['message']['chat']['id']
# print(TelegramBot.getUpdates()[size-1]['message']['entities'][0])
for i in range(0,index -1):
     print(telepot.glance(AllData[i]['message']))
# while True:
#     print("Initial:         " ,initialTime)
#     print(AllData[-1]['message']['date'])
#     AllData = TelegramBot.getUpdates()
#     if initialTime < AllData[-1]['message']['date']:
#         data = AllData[index]
#         chatID = data['message']['chat']['id']
#         order = data['message']['text']
#         string = "Counter: " + str(index+1) + " , You Said: ... " + order
#         TelegramBot.sendMessage(chatID, string)
#         print("*******************************sent*************************")
#         index += 1
#         initialTime  = data['message']['date']
#     time.sleep(2)

import telebot
import requests
import time

API_KEY = input("Enter the API key: ")
bot = telebot.TeleBot(API_KEY)
res = requests.get(
    "https://api.telegram.org/bot{}/getUpdates".format(API_KEY)).json()
print(res)

id = input("Enter the chat id: ")
message = input("Write the message: ")

#sending messages with bot
# add data to history.txt file
for i in range(10):
    bot.send_message(id, message)
    time.sleep(30)

# add data to history.txt file
file = open('history.txt', 'a')
m = []
m.append(id + '\t\t')
m.append(message + '\n')
print(m)
file.writelines(m)
file.close()
print("Messages sent successfully !")

# add data to chats.txt
file = open('chat.txt', 'a')
m = []
try:
    m.append(str(res['result'][0]['message']['chat']['id']) + '\t\t')
    m.append(res['result'][0]['message']['chat']['title'] + '\t\t')
    m.append(res['result'][0]['message']['chat']['username'] + '\t\t')
    m.append(res['result'][0]['message']['chat']['text'] + '\t\t')
    m.append(res['result'][0]['message']['chat']['type'] + '\n')
except Exception as k:
    print(k)
print(m)
file.writelines(m)
file.close()

bot.polling()

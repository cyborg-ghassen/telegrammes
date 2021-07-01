import telebot
import requests
import time


API_KEY = input("Enter the API key: ")
bot = telebot.TeleBot(API_KEY)
res = requests.get(
    "https://api.telegram.org/bot{}/getUpdates".format(API_KEY)).json()
print(res)


def send(id, message):
    #sending messages with bot
    # add data to history.txt file
    for i in range(10):
        bot.send_message(id, message)
        time.sleep(30)
        print("Message {} sent successfully !".format(i))

    # add data to history.txt file
    file = open('history.txt', 'a')
    m = []
    m.append(id + '\t\t')
    m.append(message + '\n')
    print(m)
    file.writelines(m)
    file.close()


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


# search function
def rech(A, e):
    for i in A:
        if i == e:
            return True
    return False,e


choice = int(input("Enter your choice send new message or send an existing one (write 1 or 2): "))
if choice == 1:
    id = input("Enter the chat id: ")
    message = input("Write the message: ")
    send(id, message)
elif choice == 2:
    id = int(input("Enter the id of the message: "))
    id_chat = input("Enter the chat id: ")
    f = open("messages.txt", 'r')
    l = f.readlines()
    x,y = rech(l, id)
    for i in range(1, len(l)):
        s = l[i].split(',')
    send(id_chat, s[1])

bot.polling()

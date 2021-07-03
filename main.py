import time
import random
import csv
import sys
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.types import InputPeerUser
from telethon.sync import TelegramClient
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import telebot
import requests

api_id = <your_api_id>
api_hash = '<your_api_hash>'
phone = '+216<your_phone_number>'
SLEEP_TIME = 3
client = TelegramClient(phone, api_id, api_hash)
groups = []
chats = []
last_date = None
chunk_size = 200

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))

chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue





# search function
def rech(A, e):
    for i in A:
        if i == e:
            return True
    return False, e


def save(id, message):
    to = open("history.txt", "a")
    l = []
    l.append(str(id) + "\t\t")
    l.append(message + "\n")
    to.writelines(l)

choice = int(input("Send a new message or an existing one (1 or 2): "))
if choice == 1:
    message = input("write the message: ")
elif choice == 2:
    id = int(input("Enter the id of the message: "))
    f = open("messages.txt", "r")
    l = f.readlines()
    x, y = rech(l, id)
    for i in range(1, len(l)):
        s = l[i].split(',')
    message = s[1]

i = 0
for g in groups:
    user = client.get_dialogs()
    try:
        save(user[0].id, message)
        for i in range(3):
            print("Sending Message to:", user[0].name)
            client.send_message(user[0].id, message)
            client.send_message(user[0].id, message)
            print("Waiting {} seconds".format(SLEEP_TIME))
            time.sleep(SLEEP_TIME)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        client.disconnect()
        sys.exit()
    except Exception as ee:
        print(ee)
        continue
    i += 1
    continue

client.disconnect()

import time
import sys
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 6064139
api_hash = 'e17f8cdd2dc3ffe5d8ec5752908976d2'
phone = '+21699245442'
SLEEP_TIME = 3
client = TelegramClient(phone, api_id, api_hash)
groups = []
chats = []
last_date = None
chunk_size = 200

# connect client
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

# get list of chats
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue


# function save to file
def save(id, message):
    to = open("history.txt", "a")
    l = []
    l.append(str(id) + "\t\t")
    l.append(message + "\n")
    to.writelines(l)


for g in chats:
    user = client.get_dialogs()
for i in range(len(chats)):
    print("{} - {}".format(i, user[i].name))
ch = int(input("Enter the group number: "))
with open("message.txt", "r", encoding="utf-8") as f:
    for l in f.readlines():
        # send message
        try:
            save(user[ch].id, l)
            for j in range(10):
                print("Sending Message to:", user[ch].name)
                client.send_message(user[ch].id, l)
                print("Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            client.disconnect()
            sys.exit()
        except Exception as ee:
            print(ee)
            continue

client.disconnect()

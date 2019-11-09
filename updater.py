import json
import requests
from chat import chat

class updater:
    def __init__(self, token):
        self.site = "https://api.telegram.org/bot" + token
        self.chats = []
        self.update()

    def update(self):
        chats = []
        messages = json.loads((requests.get(self.site+"/getupdates")).text)
        if messages["result"] != []:
            requests.get(self.site+"/getupdates?offset="+str(messages["result"][len(messages["result"])-1]["update_id"]+1))
            while(messages["result"] != []):
                temp_message = messages["result"].pop(0)
                for obj in chats:
                    if obj.id == temp_message["message"]["chat"]["id"]:
                        obj.append(temp_message)
                        temp_message = 1
                        break
                if temp_message != 1:
                    chats.append(chat(temp_message))
        self.chats = chats
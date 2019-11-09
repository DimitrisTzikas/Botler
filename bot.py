import json
import requests as req
from user_list import user_list

#TODO I should make better error reports

class bot:
    def __init__(self, token, messages, user_list_file_path):
        self.site = "https://api.telegram.org/bot"+token
        bot_info = json.loads((req.get(self.site+"/getMe")).text)["result"]
        self.name = bot_info["first_name"]
        self.username = bot_info["username"]
        self.messages = messages.messages
        self.chat_id = messages.id
        self.user_list = user_list(user_list_file_path)
        self.run()

        

    def send_message(self, chat_id, text_message):
        try:
            req.get(self.site + "/sendMessage?chat_id=" + str(chat_id) + "&text=" + text_message)
        except:
            raise ValueError("Sending message failed")

    def command_handler(self, message):
        # user_list commands
        if message in ("/addUser", "/addUser@" + self.username):
            # TODO CREATE USER
            self.send_message(self.get_last_message_chat_id(), str(self.user_list.get_users()))
        elif message in ("/removeUserById", "/removeUserById@" + self.username,):
            self.send_message(self.get_last_message_chat_id(), "Type the user's id")
            # TODO REMOVE USER
            self.send_message(self.get_last_message_chat_id(), str(self.user_list.get_users()))
        elif message in ("/removeUserByUsername", "/showUsers@" + self.username):
            # TODO REMOVE USER BY USERNAME
            self.send_message(self.get_last_message_chat_id(), str(self.user_list.get_users()))
        elif message in ("/showUsers", "/showUsers@" + self.username):
            self.send_message(self.get_last_message_chat_id(), str(self.user_list.get_users()))

    def run(self):
        self.send_message(self.chat_id, str(self.messages[0]["message"]["text"]))
from bot import bot
from messenger import messenger

class handler:
    def __init__(self):
        self.bots = []
        self.messenger = messenger("837420627:AAEIggxYfp4BdZHh1xmpbzDKBfEYNTBtS5U")

    def update(self):
        for chat in self.messenger.chats:
            for bot in self.bots:
                if bot.chat_id == chat.id:
                    bot.bot("837420627:AAEIggxYfp4BdZHh1xmpbzDKBfEYNTBtS5U", chat,'/home/dimitris/Documents/Git/telegram-bot/user_list.json')        
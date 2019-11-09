class chat:
    def __init__(self, message):
        self.messages = [message]
        self.id = message["message"]["chat"]["id"]

    def append(self, message):
        self.messages.append(message)
    
    def pop(self):
        return self.messages.pop(0)
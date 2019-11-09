import json

class user_list:

    def __init__(self, user_list_file_path):
        with open(user_list_file_path) as file:
            self.user_list = json.load(file)

    def save(self):
        with open('user_list.json', 'w') as file:
            json.dump(self.user_list, file)
    
    def add_user(self, id, is_bot, first_name, last_name, username):
        user = {}
        user["id"] = id
        user["is_bot"] = is_bot
        user["first_name"] = first_name
        user["last_name"] = last_name
        user["username"] = username
        self.user_list["users"].append(user)
        self.save()

    def remove_user_by_id(self, id):
        for element in range(len(self.user_list["users"])):
            if self.user_list["users"][element]["id"] == id:
                self.user_list["users"].pop(element)
                break
        self.save()
    
    def remove_user_by_username(self, username):
        for element in range(len(self.user_list["users"])):
            if self.user_list["users"][element]["username"] == username:
                self.user_list["users"].pop(element)
                break
        self.save()

    def get_users(self):
        return self.user_list["users"]
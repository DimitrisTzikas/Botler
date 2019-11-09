# Documentation

- [Overview](#overview)
- Classes
    - [bot](###bot)
    - [user_list](###user_list)

## Overview

## Classes
---

### bot
---

### user_list
#### Variables
- user_list
    - Json object
    - Contains user information

#### Methods
- save()
    - Saves the object of the variable user_list to file (user_list.json)
- add_user(id, is_bot, first_name, last_name, username)
    - Adds a user to the list
    - int id
    - boolean is_bot
    - string first_name, last_name, username
- remove_user_by_id(id)
    - Removes a user from file using the id
    - int id
- remove_user_by_username(username)
    - Removes a user from file using the username
- get_users()
    - Returns the user list (json objectxs)

#### Files
- user_list.json
- File example
```
{"users": [
    {"id": 0, "is_bot": false, "first_name": "user1", "last_name": "last1", "username": "username1"},
    {"id": 1, "is_bot": false, "first_name": "user2", "last_name": "last2", "username": "username2"},
    {"id": 2, "is_bot": false, "first_name": "user3", "last_name": "last3", "username": "username3"}
    ]}
```
---
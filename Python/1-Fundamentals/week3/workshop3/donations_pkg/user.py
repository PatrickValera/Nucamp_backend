def login(database, username, password):
    if username in database.keys():
        if database[username] == password:
            print(f"Welcome back {username}")
            return(username)
        else:
            print(f"Incorrect password for {username}")
            return("")
    else:
        print("User not found. Please register")
        return("")

def register(database,username):
    if username in database.keys():
        print("Username already register")
        return ""
    else:
        print(f"Username {username} register!")
        return username
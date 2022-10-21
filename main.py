import json

username = input("what is your name?")

filename = "username.json"
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"we will remember you when you come back, {username}")

with open(filename, "r") as f:
    username = json.load(f)
    print(f"welcome back {username}")

 ################## Refactoring ##############################
def greet_user():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"we will remember you when you come back, {username}")
    else:
        print(f"weclome back {username}")
greet_user()

def get_stored_username():
    """Get stored username if available"""
    filename = "username.json"
    try:
        with open(filename) as g:
            username = json.load(g)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """prompt new username"""
    username = input("what is your name? ")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greetings():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"welcome back, {username}")
    else:
        username= get_new_username()
        print(f"we will remember you when you come back, {username}")
greetings()
import json


# 100% working



user_info = "user_data.json"

def login():
    try:
        with open(user_info, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No users found")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user.get("username") == username and user.get("password") == password:
            print("Login successful!")
            from todo_func import user_menu_todo
            user_menu_todo()
            return
    print("Login or password incorrect.")


def registering_user():
    try:
        with open(user_info, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    while True:
        username = input("New username: ")
        if not any(user.get("username") == username for user in users):
            break
        print("Username already exists. Try again.")

    password = input("New password: ")
    new_user = {"username": username, "password": password}
    users.append(new_user)

    try:
        with open(user_info, 'w') as f:
            json.dump(users, f, indent=4)
        print("User registered successfully.")
    except Exception as e:
        print(f"Error saving user data: {e}")
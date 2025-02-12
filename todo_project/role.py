import json

admin_data = "admin_data.json"

class Admin:
    @staticmethod
    def register_admin():
        # registering
        # working 100%
        try:
            with open(admin_data, 'r') as f:
                admins = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            admins = []
        username = input("New admin username: ")
        if any(admin.get("username") == username for admin in admins):
            print("Username already exists.")
            return
        password = input("New admin password: ")
        new_admin = {"username": username, "password": password}
        admins.append(new_admin)
        try:
            with open(admin_data, 'w') as f:
                json.dump(admins, f, indent=4)
            print("Admin registered successfully.")
        except Exception as e:
            print(f"Error saving admin data: {e}")

    @staticmethod
    def verify_admin_password(username, password):
        # hash chcker
        try:
            with open(admin_data, 'r') as f:
                admins = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

        for admin in admins:
            if admin.get("username") == username and admin.get("password") == password:
                return True
        return False

    @staticmethod
    def admin_login():
        # chcker
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
# error in there
# handled
        if Admin.verify_admin_password(username, password):
            print("Login successful!")
            from todo_func import admin_menu_todo 
            admin_menu_todo()
            return True
        else:
            print("Login or password incorrect.")
            return False
        
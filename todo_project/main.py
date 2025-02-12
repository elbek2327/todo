# todo_project/main.py
from auth import login, registering_user
from role import Admin

# 100% working
# menu working perfectly
def menu():
    while True:
        print("\nChoose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Admin Login")
        print("4. Admin Register")
        print("'s'. Exit")

        try:
            choice = input("Enter your choice: ")
            if choice == '1':
                login()
            elif choice == '2':
                registering_user()
            elif choice == '3':
                Admin.admin_login()
            elif choice == '4':
                Admin.register_admin()
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    menu()
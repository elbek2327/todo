filename = 'todo.json'
import json
from datetime import datetime


class CRUD:
    # for creating Id in todo_data
    def generate_unique_id(todos):
        if not todos:
            return 1
        else:
            max_id = max(todo.get("id", 0) for todo in todos) 
            return max_id + 1
        

    # reading by id
    def read_todos():
        try:
            with open(filename, 'r') as f:
                todos = json.load(f)
                if not todos:
                    print("No todos found.")
                    return

                for todo in todos:
                    CRUD.print_todo(todo) 
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"File {filename} not found or invalid. No todos to read.")

    def print_todo(todo):
        print(f"Todo ID: {todo.get('id', 'N/A')}") 
        for key, value in todo.items():
            if key != 'id': 
                print(f"  {key.capitalize()}: {value}")
        print("-" * 20)


    # create to do working
    def creating_todo():
        try:
            with open(filename, 'r') as f:
                todos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            todos = []

        todo_data = {}
        todo_data["id"] = CRUD.generate_unique_id(todos) # Generate a unique ID
        todo_data["todo_name"] = input("Enter todo name: ")
        todo_data["todo_title"] = input("Enter todo title: ")
        todo_data["todo_description"] = input("Enter todo description: ")
        todo_data["todo_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todos.append(todo_data)
        with open(filename, 'w') as f:
            json.dump(todos, f, indent=4)
        print(f"Todo created successfully with ID: {todo_data['id']}")


    # updating todo working 
    def update_todo():
        try:
            with open(filename, 'r') as f:
                todos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"File {filename} not found or invalid. Cannot update.")
            return
        todo_id = int(input("Enter the ID of the todo to update: "))
        for todo in todos:
            if todo.get("id") == todo_id:
                print("Found todo. Enter new details (or press Enter to keep current):")
                todo["todo_name"] = input(f"New name ({todo.get('todo_name')}) : ") or todo.get('todo_name')
                todo["todo_title"] = input(f"New title ({todo.get('todo_title')}) : ") or todo.get('todo_title')
                todo["todo_description"] = input(f"New description ({todo.get('todo_description')}) : ") or todo.get('todo_description')
                todo["todo_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break  # Exit 
        else: 
            print(f"Todo with ID {todo_id} not found.")
            return

        with open(filename, 'w') as f:
            json.dump(todos, f, indent=4)
        print("Todo updated successfully!")


    # deleting to do by id
    def delete_todo():
        try:
            with open(filename, 'r') as f:
                todos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"File {filename} not found or invalid. Cannot delete.")
            return
        todo_id = int(input("Enter the ID of the todo to delete: "))
        for i, todo in enumerate(todos):
            if todo.get("id") == todo_id:
                del todos[i]
                break
        else:
            print(f"Todo with ID {todo_id} not found.")
            return

        with open(filename, 'w') as f:
            json.dump(todos, f, indent=4)
        print("Todo deleted successfully!")    
        
        
def admin_menu_todo():
    while True:
        print("\nAdmin Menu")
        print("1. Create Todo")
        print("2. Update Todo")
        print("3. Delete Todo")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            CRUD.creating_todo()
        elif choice == '2':
            CRUD.update_todo()
        elif choice == '3':
            CRUD.delete_todo()
        elif choice == '4':
            from main import menu
            menu()

def user_menu_todo():
    while True:
        print("\nUser Menu")
        print("1. View Todos")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            CRUD.read_todos()
        elif choice == '2':
            from main import menu
            menu()
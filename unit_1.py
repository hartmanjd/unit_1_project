import json
import hashlib



def registration():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    return username, password

def login():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    hashed_password = hash_password(password)

    try:
        with open('user_data.json', 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        print("No users registered yet.")
        return False

    for user in user_data:
        if user['username'] == username and user['password'] == hashed_password:
            print("Login successful!")
            return True
        
            

    print("Invalid username or password.")
    return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_user_data(username, password):
    try:
        with open('user_data.json', 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = []
    for user in user_data:
        if user['username'] == username:
            print("Username already exists. Please choose a different username.")
            return False
                   
    user_data.append({'username': username, 'password': hash_password(password)})  

    with open('user_data.json', 'w') as f:
        json.dump(user_data, f, indent=2)
    return True

while True:
    choice = input("Do you want to register or login? (register/login): ")
    if choice == 'register':
        while True:
            username, password = registration()
            if save_user_data(username, password):
                print("User saved successfully!")
                break
        
           
    elif choice == 'login':
        if login():
            break

def main_menu():
    print('Please choose an option:')
    print()
    print('1. Add a Task')
    print('2. View Tasks')
    print('3. Mark a Task as Completed')
    print('4. Delete a Task')
    print('5. Logout')

def add_task():
    try:
        task = input('Enter the task you want to add: ')
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    tasks.append({'task': task, 'completed': False})
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)
    print("Task added successfully!")

def view_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start = 1):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f"{index}. {task['task']} - {status}")


while True:
    print()
    main_menu()
    menu_choice = input('Enter your choice (1-5): ')
    print()
    while True:
        if menu_choice == '1':
            add_task()
            break
        elif menu_choice == '2':
            view_tasks()
            break
        elif menu_choice == '3':
            mark_task_completed()
        elif menu_choice == '4':
            delete_task()
        elif menu_choice == '5':
            print("Logging out...")
            break





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




import json

def registration():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    return username, password

def save_user_data(username, password):
    try:
        with open('user_data.json', 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = []
               
    user_data.append({'username': username, 'password': password})  

    with open('user_data.json', 'w') as f:
        json.dump(user_data, f, indent=2)
    
username, password = registration()
if save_user_data(username, password):
    print("User saved successfully!")
    break

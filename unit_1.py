import json

def registration():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    return username, password

def save_user_data(username, password):
    user_data = {'username': username, 'password': password}
    with open('user_data.json', 'w') as f:
        json.dump(user_data, f)


import json

data_file = 'user_data.json'

def load_user_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)

user_data = load_user_data()

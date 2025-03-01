import json

def save_password(site, username, encrypted_password):
    password_data = {
        "site": site,
        "username": username,
        "password": encrypted_password.decode()
    }
    
    with open("passwords.json", "a") as file:
        json.dump(password_data, file)
        file.write("\n")  # Запись пароля в каждую новую строку

def load_passwords():
    passwords = []
    with open("passwords.json", "r") as file:
        for line in file:
            passwords.append(json.loads(line))
    return passwords

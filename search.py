def find_password(site):
    passwords = load_passwords()
    for password_data in passwords:
        if password_data['site'] == site:
            return password_data
    return None

def update_password(site, new_encrypted_password):
    passwords = load_passwords()
    updated = False
    for password_data in passwords:
        if password_data['site'] == site:
            password_data['password'] = new_encrypted_password.decode()
            updated = True
            break
    
    if updated:
        with open("passwords.json", "w") as file:
            for password in passwords:
                json.dump(password, file)
                file.write("\n")

# Пример использования:
generate_key()  # Делается один раз для генерации ключа
key = load_key()
new_password = generate_password()
encrypted_new_password = encrypt_password(new_password, key)
save_password("example.com", "user1", encrypted_new_password)

# Найти и обновить пароль
password_data = find_password('example.com')
if password_data:
    print(f"Username: {password_data['username']}, Encrypted Password: {password_data['password']}")
    
    new_password = generate_password()
    new_encrypted_password = encrypt_password(new_password, key)
    update_password('example.com', new_encrypted_password)

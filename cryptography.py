from cryptography.fernet import Fernet

# Генерация и сохранение ключа
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Загрузка ключа
def load_key():
    return open("secret.key", "rb").read()

# Шифрование паролей
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Дешифрование паролей
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

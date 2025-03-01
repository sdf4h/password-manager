# password-manager
```
# Password Manager – Генератор и менеджер паролей

**Password Manager** – это приложение для безопасного создания, шифрования, хранения и управления паролями. Оно обеспечивает высокую степень безопасности паролей с помощью современных методов шифрования и позволяет в удобной форме хранить и управлять данными.

## Функционал
- **Генерация паролей**: Случайное создание безопасных паролей с заданными параметрами (длина, наличие специальных символов и др.).
- **Шифрование паролей**: Для обеспечения сохранности данных используется библиотека `cryptography`.
- **Хранение паролей**: Данные о паролях сохраняются в файле `passwords.json`, каждый пароль сохраняется на отдельной строке.
- **Поиск и обновление паролей**: Возможность находить существующую запись по названию сайта и обновлять шифрованные пароли.

## Требования
Проект написан на Python и требует установленной версии Python 3.6 или выше.

### Библиотеки
- `cryptography` – Для шифрования паролей.
  
Установить библиотеку можно командой:
```bash
pip install cryptography
```

## Установка и запуск
1. Склонируйте репозиторий или загрузите проект.
2. Установите требуемые зависимости с помощью pip:
   ```bash
   pip install cryptography
   ```
3. Сгенерируйте секретный ключ для шифрования:
   ```python
   from cryptography.fernet import Fernet
   key = Fernet.generate_key()
   with open("secret.key", "wb") as key_file:
       key_file.write(key)
   ```
4. Запустите приложение, используя интерфейс командной строки или добавьте его в ваш проект.

## Примеры использования
### Генерация и шифрование пароля
```python
from cryptography.fernet import Fernet
from password_manager import generate_password, encrypt_password

# Генерация ключа
generate_key()
key = load_key()

# Создаем новый пароль
password = generate_password(length=16, include_special_chars=True)
encrypted_password = encrypt_password(password, key)
print(f"Сгенерированный пароль: {password}")
print(f"Шифрованный пароль: {encrypted_password}")
```

### Сохранение и поиск пароля
```python
from password_manager import save_password, find_password

# Сохранение пароля
save_password("example.com", "test_user", encrypted_password)

# Поиск существующего пароля
password_data = find_password("example.com")
if password_data:
    print(f"Сайт: {password_data['site']}")
    print(f"Логин: {password_data['username']}")
    print(f"Шифрованный пароль: {password_data['password']}")
```

### Обновление пароля
```python
from password_manager import update_password

new_password = generate_password(length=12, include_special_chars=False)
new_encrypted_password = encrypt_password(new_password, key)
update_password("example.com", new_encrypted_password)
print("Пароль успешно обновлен!")
```

## Структура проекта
```
password_manager/
│
├── password_manager.py       # Основной функционал приложения
├── passwords.json            # Файл для хранения паролей
├── secret.key                # Файл с секретным ключом шифрования
├── README.md                 # Документация по проекту
```

## Предостережения
- **Не делитесь файлом `secret.key`!** Это главный ключ шифрования, утечка которого приведет к скомпрометированию всех ваших паролей.
- Регулярно обновляйте свои пароли и используйте уникальные пароли для каждого сайта/сервиса.

## Планы по доработке
1. Добавить возможность использования базы данных SQLite вместо JSON для больших объемов данных.
2. Создать полноценный интерфейс командной строки (CLI).
3. Реализовать графический интерфейс (GUI) для доступа к менеджеру паролей.
4. Добавить поддержку двухфакторной аутентификации.

## Авторы
Этот проект был разработан в качестве учебного примера для управления паролями. Если у вас есть предложения или вопросы, вы можете связаться с разработчиком по электронной почте.

## Лицензия
Этот проект находится в общем доступе и может свободно использоваться (MIT License).
```

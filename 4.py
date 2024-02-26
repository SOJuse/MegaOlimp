# Подключаем необходимые библиотеки
import csv
import random


# Функция генерации логина
def create_login(name):
    login = f"{name.split()[0]}_{name.split()[1][0]}{name.split()[2][0]}"
    return login


# Функция генерации пароля
def create_password():
    alpha = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890'
    password = random.choices(alpha, k=10)
    return ''.join(password)


# Считываем файл
with open('scientist.txt', 'r', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))  # Считываем файл как csv документ
    # Дополним считаные данные
    for person in reader:
        person['login'] = create_login(person['ScientistName'])
        person['password'] = create_password()
# Записываем полученые данные в новый файл
with open('scientist_password.csv', 'w', encoding='utf-8', newline='') as file:
    names_columns = ['ScientistName', 'preparation', 'date', 'components', 'login', 'password']
    writer = csv.DictWriter(file, fieldnames=names_columns, delimiter='#')
    writer.writeheader()
    writer.writerows(reader)

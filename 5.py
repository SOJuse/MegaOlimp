# Подключаем необходимые библиотеки
import csv
import random

# Считываем файл
with open('scientist.txt', 'r', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))  # Считываем файл как csv документ
    table = [x for x in range(1024)]
    random.shuffle(table)
    # Создадим хеши и дополним данные
    for person in range(len(reader)):
        hashes = 0
        for letter in reader[person]['ScientistName']:
            hashes += table[ord(letter) % 1024]
        reader[person] = {'hash': hashes % 2048, 'ScientistName': reader[person]['ScientistName'],
                          'preparation': reader[person]['preparation'], 'date': reader[person]['date'],
                          'components': reader[person]['components']}
# Записываем полученые данные в новый файл
with open('cientist _with_hash.csv', 'w', encoding='utf-8', newline='') as file:
    names_columns = ['hash', 'ScientistName', 'preparation', 'date', 'components']
    writer = csv.DictWriter(file, fieldnames=names_columns, delimiter='#')
    writer.writeheader()
    writer.writerows(reader)

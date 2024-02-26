# Подключаем необходимые библиотеки
import csv


# Функция двоичного поиска
def bin_search(date, alist):
    date1 = date.split('.')
    date = f'{date1[2]}-{date1[1]}-{date1[0]}'
    L = 0
    R = len(alist) - 1
    while L <= R:
        m = L + (R - L) // 2
        if alist[m]['date'] > date:
            R = m - 1
        elif alist[m]['date'] < date:
            L = m + 1
        else:
            return alist[m]
    return 0


# Считываем файл
with open('scientist.txt', 'r', encoding='utf-8') as file:
    names_columns = ['ScientistName', 'preparation', 'date', 'components']
    reader = list(csv.DictReader(file, delimiter='#'))  # Считываем файл как csv документ
    date = input()
    while date != 'эксперимент':
        answer = bin_search(date, reader)
        if answer:
            fio = f"{answer['ScientistName'].split()[0]} {answer['ScientistName'].split()[1][0]}.{answer['ScientistName'].split()[2][0]}."
            print(f'Ученый {fio} создал препарат: {answer["preparation"]} - {answer["date"]}')
        else:
            print('В этот день ученые отдыхали')
        date = input()

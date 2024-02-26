# Подключаем необходимые библиотеки
import csv
import random


# Функция быстрой сортировки
def quicksort(n):
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        q = random.choice([x['date'] for x in n])
        for a in n:
            if a['date'] < q:
                l_list.append(a)
            elif a['date'] > q:
                r_list.append(a)
            else:
                m_list.append(a)
        return quicksort(l_list) + m_list + quicksort(r_list)


# Считываем файл
with open('scientist.txt', 'r', encoding='utf-8') as file:
    names_columns = ['ScientistName', 'preparation', 'date', 'components']
    reader = list(csv.DictReader(file, delimiter='#'))  # Считываем файл как csv документ
    reader = quicksort(reader)
# Перезаписываем файл (в задание 2 не было сказанно, что нужно перезаписывать файл, но из формулировки 2 и 3 задания, мне показалось, что это необходимо)
with open('scientist.txt', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=names_columns, delimiter='#')
    writer.writeheader()
    writer.writerows(reader)

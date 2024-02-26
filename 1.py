# Подключаем необходимые библиотеки
import csv

# Считываем файл
with open('scientist.txt', 'r', encoding='utf-8') as file:
    names_columns = ['ScientistName', 'preparation', 'date', 'components']
    reader = list(csv.DictReader(file, delimiter='#'))  # Считываем файл как csv документ
    reader = sorted(reader, key=lambda x: (x['date']))  # Сортируем по дате по неубыванию
    preparations = []
    creations = []
    poddelniki = []
    for creation in reader:
        if creation['preparation'] not in preparations:
            creations.append(creation)
            preparations.append(creation['preparation'])
        if creation['preparation'] == 'Аллопуринол':
            poddelniki.append(creation)
    # Выводим разработчиков Аллопуринола
    print('Разработчиками Аллопуринола были такие люди')
    for poddelnik in poddelniki:
        print(f'{poddelnik["ScientistName"]} - {poddelnik["date"]}')
    print(f'Оригинальный рецепт принадлежит: {poddelniki[0]["ScientistName"]}')
# Записываем полученые данные в новый файл
with open('scientist_origin.txt', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=names_columns, delimiter='#')
    writer.writeheader()
    writer.writerows(creations)

'''
Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи,
присваивая этим ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом
объекте, но отсутствует в данном. Программа должна создать список с обновленными JSON-объектами и записать
его в файл updated_people.json.
'''
import json

with open('people.json', 'r', encoding='utf-8') as file,\
     open('updated_people.json', 'w', encoding='utf-8') as new_file:
    data = json.load(file)
    pattern = {key: None for key in max(data, key=len).copy()}

    for i in range(len(data)):
        for key_pattern in pattern:
            data[i].setdefault(key_pattern)

    json.dump(data, new_file, indent=4)

# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json


def apdate_data(data):
    name = input('Введите ваше имя: ')
    id = int(input('Введите ваш айди: '))
    level = input('Введите ваш уровень доступа: ')

    temp = data.get(level, [])
    temp.append({'name': name, 'id': id})
    data[level] = temp

    return data


while True:
    try:
        with open('data_base.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data = apdate_data(data)

    with open('data_base.json', 'w') as f:
        data = json.dump(data, f, indent=4)

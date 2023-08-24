# Напишите функцию, которая сереализует содержимое
# текущей директории в json-файл.
# В файле должен храниться список словарей,
# словарь описывает элемент внутри директории: имя, расширение, тип.
# Если элемент - директория, то только тип и имя.
# Пример результата для папки, где лежит файл test.txt
# и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]

import os
import json
import sys


def generate_directory_info(path):
    info = {'name': os.path.basename(path)}

    if os.path.isdir(path):
        info['type'] = 'directory'
        info['contents'] = ([generate_directory_info(os.path.join(path, f))
                             for f in os.listdir(path)])
    else:
        info['extension'] = os.path.splitext(path)[1]
        info['type'] = 'file'

    return info


def save_info_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    try:
        target_directory = sys.argv[1]
    except IndexError:
        target_directory = os.getcwd()

    json_filename = 'directory_info.json'
    directory_info_data = generate_directory_info(target_directory)
    save_info_to_json(directory_info_data, json_filename)

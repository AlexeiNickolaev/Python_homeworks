# Напишите функцию, которая принимает на вход
# строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь,
# имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: (' c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


import os


def parse_file_path(file_path):
    path, full_file_name = os.path.split(file_path)
    file_name, extension = os.path.splitext(full_file_name)
    return path, file_name, extension


string = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
result = parse_file_path(string)
print(result)

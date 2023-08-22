# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
# Чтобы записать байты можно использовать список с числами и функцию bytes

from random import randint, choice
import string


def generate_files(extension: str, min_len_name=6, max_len_name=30,
                   min_random_bytes=256, max_random_bytes=4096, num_files=42):
    for _ in range(num_files):
        name_length = randint(min_len_name, max_len_name)
        file_name = ''.join(choice(string.ascii_lowercase)
                            for _ in range(name_length)) + '.' + extension

        file_size = randint(min_random_bytes, max_random_bytes)
        file_data = bytes([randint(0, 255) for _ in range(file_size)])

        with open(file_name, "wb") as file:
            file.write(file_data)


if __name__ == "__main__":
    generate_files("txt", num_files=3)

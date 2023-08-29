# Создать декоратор для использования кэша.
# Т.е. сохранять аргументы и результаты в словарь,
# если вызывается функция с агрументами,
# которые уже записаны в кэше - вернуть результат из кэша,
# если нет - выполнить функцию. Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.


import json
from typing import Callable


def json_cache(func: Callable):
    try:
        with open(f'{func.__name__}_cache.json', 'r') as cache_file:
            cache = json.load(cache_file)
    except FileNotFoundError:
        cache = {}

    def wrapper(*args, **kwargs):
        args_key = json.dumps(args) + json.dumps(kwargs)
        if args_key in cache:
            print('Результат из кэша: ')
            return cache[args_key]
        else:
            print('Вычисляю результат...')
            result = func(*args, **kwargs)
            cache[args_key] = result
            with open(f'{func.__name__}_cache.json', 'w') as cache_file:
                json.dump(cache, cache_file, indent=4)
            return result

    return wrapper


@json_cache
def custom_sum(*args, **kwargs):
    return sum(args)


if __name__ == "__main__":
    print(custom_sum(3, 3))
    print(custom_sum(2, 7, 1))
    print(custom_sum(6, 4))
    print(custom_sum(1, 2, 3, 4))
    print(custom_sum(8, 2))
    print(custom_sum(4, 5, 6, 7))

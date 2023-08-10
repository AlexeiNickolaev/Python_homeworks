# Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую
# словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def reverse_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, bool)):
            result[value] = key
        else:
            result[str(key)] = value
    return result


kwargs_dict = reverse_kwargs(rev=True, acc="YES", stroka=4)
print(kwargs_dict)

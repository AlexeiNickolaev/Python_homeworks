# 1. Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# 2. В модуль с проверкой даты добавьте возможность запуска в терминале
# с передачей даты на проверку.

from sys import argv

FIRST_DAY = 1
LAST_DAY = 31
FIRST_MONTH = 1
LAST_MONTH = 12
FIRST_YEAR = 1
LAST_YEAR = 9999


def leap_year(date: str) -> bool:
    day, month, year = list(map(int, date.split('.')))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def valid_date(date: str) -> bool:
    day, month, year = list(map(int, date.split('.')))
    if (FIRST_DAY <= day <= LAST_DAY and
        FIRST_MONTH <= month <= LAST_MONTH and
            FIRST_YEAR <= year <= LAST_YEAR):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if leap_year(date):
            days_in_month[2] = 29

        return day <= days_in_month[month]

    return False


if __name__ == '__main__':
    print(argv)
    print(valid_date(argv[1]))
    print(leap_year(argv[1]))

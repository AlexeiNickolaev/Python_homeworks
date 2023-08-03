# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def integer_to_hex(num: int, base=16):
    hex_chars = '0123456789abcdef'
    result_str = ''
    while num > 0:
        result_str = hex_chars[num % base] + result_str
        num //= base
    return result_str


num = 111
print(integer_to_hex(num))
print(hex(num))

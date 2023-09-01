# Возьмите  любые задания из прошлых семинаров (например сериализация данных),
#  которые вы уже решали. Превратите функции в методы класса,
# а параметры в свойства. Задания должны решаться
# через вызов методов экземпляра.
# (Например: Дроби дз2)
# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import math


class Fractions:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def calculate_sum(self, other):
        new_num = (self.numerator * other.denominator +
                   self.denominator * other.numerator)
        new_den = self.denominator * other.denominator
        reduction = math.gcd(new_num, new_den)
        return Fraction(new_num // reduction, new_den // reduction)

    def calculate_product(self, other):
        prod_num = self.numerator * other.numerator
        prod_den = self.denominator * other.denominator
        reduction = math.gcd(prod_num, prod_den)
        return Fraction(prod_num // reduction, prod_den // reduction)


fraction_a = Fractions(2, 3)
fraction_b = Fractions(8, 9)

sum_result = fraction_a.calculate_sum(fraction_b)
product_result = fraction_a.calculate_product(fraction_b)

print(f'Сумма: {sum_result.numerator}/{sum_result.denominator}')
print(f'Произведение: {product_result.numerator}/{product_result.denominator}')

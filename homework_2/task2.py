# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction as F


def fractions(fraction_a, fraction_b):
    numerator_1_str, denominator_1_str = map(str.strip, fraction_a.split('/'))
    numerator_2_str, denominator_2_str = map(str.strip, fraction_b.split('/'))

    numerator_1, denominator_1 = int(numerator_1_str), int(denominator_1_str)
    numerator_2, denominator_2 = int(numerator_2_str), int(denominator_2_str)

    sum_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    sum_denominator = denominator_1 * denominator_2
    sum_result = (sum_numerator, sum_denominator)

    prod_numerator_1 = numerator_1 * numerator_2
    prod_denominator_1 = denominator_1 * denominator_2
    product_result = (prod_numerator_1, prod_denominator_1)

    return sum_result, product_result


fraction_a = '2/3'
fraction_b = "8/9"

sum_result, product_result = fractions(fraction_a, fraction_b)
f1, f2 = F(fraction_a), F(fraction_b)

print(f"{fraction_a} + {fraction_b} = {f1 + f2}")
print(f"{fraction_a} * {fraction_b} = {f1 * f2}")

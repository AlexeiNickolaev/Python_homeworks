# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def find_duplicates(listt):
    return list({el for el in listt if listt.count(el) > 1})


listt = [1, 2, 3, 1, 2, 4, 5]
print(f'{listt} -> {find_duplicates(listt)}')

# Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str
# с указанием процентов вида “10.25%”. В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
# Ввод:
# name_list = ['Vlad', 'Den', 'Alex']
# salary_list = [1000, 2000, 3000]
# extra_list = ['10.25%', '15%', '20%']
# Вывод:
# {'Vlad': 102.5, 'Den': 300.0, 'Alex': 600.0}

def calculate_bonus(salary, percentage):
    return salary * float(percentage.strip('%')) / 100


def generate_bonus_dictionary(names, salaries, bonuses):
    bonus_dict = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        bonus_amount = calculate_bonus(salary, bonus)
        bonus_dict[name] = bonus_amount
    return bonus_dict


name_list = ['Vlad', 'Den', 'Alex']
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']

bonus_dictionary = generate_bonus_dictionary(
    name_list, salary_list, extra_list)
print(bonus_dictionary)

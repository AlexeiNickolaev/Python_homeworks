# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв.

class NameValidator:
    def __set_name__(self, owner, name):
        self.param_name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.param_name)

    def __set__(self, instance, value: str):
        if not value.isalpha() or not value[0].isupper():
            raise ValueError(
                f'{self.param_name.capitalize()} должно начинаться '
                f'с заглавной буквы и содержать только буквы')
        instance.__dict__[self.param_name] = value


class Student:
    first_name = NameValidator()
    surname_name = NameValidator()
    last_name = NameValidator()

    def __init__(self, first_name, surname_name, last_name):
        self.first_name = first_name
        self.surname_name = surname_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.surname_name} {self.last_name}'


try:
    student = Student('Иван', 'Петрович', 'Иванов')
    print(student)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    student = Student('Иван', 'петрович', 'Иванов')
    print(student)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    student = Student('Иван1', 'Петрович', 'Иванов')
    print(student)
except ValueError as e:
    print(f"Ошибка: {e}")

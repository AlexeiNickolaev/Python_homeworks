# Возьмите  любые задания из прошлых семинаров (например сериализация данных),
#  которые вы уже решали. Превратите функции в методы класса,
# а параметры в свойства. Задания должны решаться
# через вызов методов экземпляра.
# (Например: Треугольник дз1)
# Треугольник существует только тогда, когда сумма
# любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if (self.a + self.b > self.c
            and self.b + self.c > self.a
                and self.a + self.c > self.b):
            return True
        else:
            return False

    def get_type(self):
        if self.check_triangle():
            if self.a == self.b == self.c:
                return 'Треугольник равносторонний'
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                return 'Треугольник равнобедренный'
            else:
                return 'Треугольник разносторонний'
        else:
            return 'Треугольник не существует'


a = 5
b = 7
c = 9

triangle = Triangle(a, b, c)
print(triangle.get_type())

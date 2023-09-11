# Возьмите 1-3 задачи из тех, что были на прошлых семинарах
# или в домашних заданиях. Напишите к ним классы исключения
# с выводом подробной информации. Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


class TriangleError(Exception):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return (f'Ошибка: Невозможно создать треугольник'
                f' с заданными сторонами {self.A}, {self.B}, {self.C}')


class NegativeSideLengthError(Exception):
    def __init__(self, param, value):
        self.param = param
        self.value = value

    def __str__(self):
        if self.param < self.value:
            return (f'Ошибка: Нельзя использовать отрицательные'
                    f' длины сторон: {self.param} < {self.value}')
        elif self.param == self.value:
            return (f'Ошибка: Нельзя использовать стороны'
                    f' с нулевой длиной: {self.param} = {self.value}')


class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise NegativeSideLengthError(min(a, b, c), 0)
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
            raise TriangleError(self.a, self.b, self.c)


a = 1
b = 1
c = 9

try:
    triangle = Triangle(a, b, c)
    print(triangle.get_type())
except NegativeSideLengthError as e:
    print(e)
except TriangleError as e:
    print(e)

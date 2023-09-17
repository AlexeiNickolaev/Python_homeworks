import logging


def log_info(text: str):
    logging.basicConfig(filename='log_triangle.log',
                        encoding='utf-8',
                        format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(text)


def log_error(text: str):
    logging.basicConfig(filename='log_triangle.log',
                        encoding='utf-8',
                        format='{asctime} {levelname:<8} функция "{funcName}()"строка {lineno:>3d} : {msg}',
                        style='{',
                        level=logging.ERROR)
    logger = logging.getLogger(__name__)
    logger.error(text)


class TriangleError(Exception):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return (f'Ошибка: Невозможно создать треугольник'
                f' с заданными сторонами {self.a}, {self.b}, {self.c}')


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
        try:
            if a <= 0 or b <= 0 or c <= 0:
                raise NegativeSideLengthError(min(a, b, c), 0)
            self.a = a
            self.b = b
            self.c = c
        except NegativeSideLengthError as e:
            log_error(str(e))

    def check_triangle(self):
        if (self.a + self.b > self.c
            and self.b + self.c > self.a
                and self.a + self.c > self.b):
            return True
        else:
            return False

    def get_type(self):
        try:
            if self.check_triangle():
                if self.a == self.b == self.c:
                    log_info('Треугольник равносторонний')
                    return 'Треугольник равносторонний'
                elif self.a == self.b or self.b == self.c or self.a == self.c:
                    log_info('Треугольник равнобедренный')
                    return 'Треугольник равнобедренный'
                else:
                    log_info('Треугольник разносторонний')
                    return 'Треугольник разносторонний'
            else:
                raise TriangleError(self.a, self.b, self.c)
        except TriangleError as e:
            log_error(str(e))


a = 7
b = 8
c = 9

try:
    triangle = Triangle(a, b, c)
    print(triangle.get_type())
except NegativeSideLengthError as e:
    print(e)
except TriangleError as e:
    print(e)

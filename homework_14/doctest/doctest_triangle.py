class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        """
        >>> Triangle(5, 7, 9).check_triangle()
        True

        >>> Triangle(1, 1, 3).check_triangle()
        False
        """
        if (self.a + self.b > self.c
            and self.b + self.c > self.a
                and self.a + self.c > self.b):
            return True
        else:
            return False

    def get_type(self):
        """
        >>> Triangle(5, 5, 5).get_type()
        'Треугольник равносторонний'

        >>> Triangle(5, 7, 7).get_type()
        'Треугольник равнобедренный'

        >>> Triangle(3, 4, 5).get_type()
        'Треугольник разносторонний'

        >>> Triangle(1, 1, 3).get_type()
        'Треугольник не существует'
        """
        if self.check_triangle():
            if self.a == self.b == self.c:
                return 'Треугольник равносторонний'
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                return 'Треугольник равнобедренный'
            else:
                return 'Треугольник разносторонний'
        else:
            return 'Треугольник не существует'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

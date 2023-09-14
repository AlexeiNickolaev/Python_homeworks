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


a = 1
b = 2
c = 6

triangle = Triangle(a, b, c)
print(triangle.get_type())

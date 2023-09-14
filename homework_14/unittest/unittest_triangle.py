import unittest


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


class TestTriangle(unittest.TestCase):
    def test_check_triangle_true(self):
        t = Triangle(5, 7, 9)
        self.assertTrue(t.check_triangle())

    def test_check_triangle_false(self):
        t = Triangle(1, 1, 3)
        self.assertFalse(t.check_triangle())

    def test_get_type_equilateral(self):
        t = Triangle(5, 5, 5)
        self.assertEqual(t.get_type(), 'Треугольник равносторонний')

    def test_get_type_isosceles(self):
        t = Triangle(5, 7, 7)
        self.assertEqual(t.get_type(), 'Треугольник равнобедренный')

    def test_get_type_scalene(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.get_type(), 'Треугольник разносторонний')

    def test_get_type_nonexistent(self):
        t = Triangle(1, 1, 3)
        self.assertEqual(t.get_type(), 'Треугольник не существует')


if __name__ == '__main__':
    unittest.main()

from task_triangle import Triangle


def test_check_triangle_true():
    t = Triangle(5, 7, 9)
    assert t.check_triangle()


def test_check_triangle_false():
    t = Triangle(1, 1, 3)
    assert not t.check_triangle()


def test_get_type_equilateral():
    t = Triangle(5, 5, 5)
    assert t.get_type() == 'Треугольник равносторонний'


def test_get_type_isosceles():
    t = Triangle(5, 7, 7)
    assert t.get_type() == 'Треугольник равнобедренный'


def test_get_type_scalene():
    t = Triangle(3, 4, 5)
    assert t.get_type() == 'Треугольник разносторонний'


def test_get_type_nonexistent():
    t = Triangle(1, 1, 3)
    assert t.get_type() == 'Треугольник не существует'

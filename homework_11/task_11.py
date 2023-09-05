# Создайте класс Матрица. Добавьте методы для:
# вывода на печать, сравнения, сложения.

import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError('Матрицы разных размеров нельзя сложить.')
        result_data = self.data + other.data
        return Matrix(result_data)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

print('Matrix 1:')
print(matrix1)

print('Matrix 2:')
print(matrix2)

if matrix1 == matrix2:
    print('Матрицы равны.')
else:
    print('Матрицы не равны.')

try:
    result_matrix = matrix1 + matrix2
    print('Результат сложения:')
    print(result_matrix)
except ValueError as e:
    print(f'Ошибка: {e}')

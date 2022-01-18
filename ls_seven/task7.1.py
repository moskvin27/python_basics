# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, line_matrix):
        self.line_matrix = line_matrix

    def __str__(self):
        for i in self.line_matrix:
            for k in i:
                print(k, end=' ')
            print()
        return ' '

    def __add__(self, other):
        for i in range(len(self.line_matrix)):
            for k in range(len(other.line_matrix[i])):
                print(self.line_matrix[i][k] + other.line_matrix[i][k], end=' ')
            print()


matrix_one = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_one)
matrix_two = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix_two)
matrix_one + matrix_two

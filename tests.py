import unittest
from main import solve_quadratic_equation,transpone_matrix

class TestSolveQuadraticEquation(unittest.TestCase):
    def test_discriminant_positive(self):
        result = solve_quadratic_equation(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))

    def test_discriminant_zero(self):
        result = solve_quadratic_equation(1, -4, 4)
        self.assertEqual(result, 2.0)

    def test_discriminant_negative(self):
        result = solve_quadratic_equation(1, 1, 1)
        self.assertIsNone(result)


class TestTransposeMatrix(unittest.TestCase):

    def test_transpose_matrix_valid(self):
        # Проверка транспонирования матрицы с допустимой размерностью
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected_result = [[1, 4], [2, 5], [3, 6]]
        result = transpone_matrix(matrix)
        self.assertEqual(result, expected_result)

    def test_transpose_matrix_empty(self):
        # Проверка транспонирования пустой матрицы
        matrix = []
        result = transpone_matrix(matrix)
        self.assertEqual(result, [])

    def test_transpose_matrix_irregular(self):
        # Проверка транспонирования матрицы с разной длиной строк
        matrix = [[1, 2, 3], [4, 5]]
        expected_result = [[1, 4], [2, 5], [3, None]]
        result = transpone_matrix(matrix)
        self.assertEqual(result, expected_result)


class TestIntegrateTrapezoidal(unittest.TestCase):
    def test_integral_of_x_squared(self):
        def f(x):
            return x ** 2
        result = integrate_trap(f, 0, 1, 0.1)
        self.assertAlmostEqual(result, 0.3333333, places=2)

    def test_integral_of_constant_function(self):
        def f(x):
            return 5
        result = integrate_trap(f, 1, 5, 1)
        self.assertEqual(result, 20)

    def test_negative_step_size(self):
        def f(x):
            return x
        result = integrate_trap(f, 0, 1, -0.1)
        self.assertEqual(result, 0)


import unittest
from main import solve_quadratic_equation


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


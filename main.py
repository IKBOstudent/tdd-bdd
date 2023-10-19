import math


def solve_quadratic_equation(a, b, c):
    if a == 0:
        ans = b / (-c)
        return ans
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def transpone_matrix(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Находим максимальную длину строки в матрице
    max_row_length = max(len(row) for row in matrix)

    transposed = [[None] * num_rows for _ in range(max_row_length)]

    for i in range(num_rows):
        for j in range(num_cols):
            if j < len(matrix[i]):
                transposed[j][i] = matrix[i][j]

    return transposed


def calculate_factorial(number):
    if number < 0:
        return None

    factorial_value = 1
    for i in range(1, number + 1):
        factorial_value *= i
    return factorial_value


def matrix_sum(matrix1, matrix2):
    # Проверяем, что размерности матриц совпадают
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None

    # Создаем пустую матрицу для результата
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Выполняем сложение элементов матриц
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


def integrate_trap(f, a, b, h):
    if h <= 0:
        return 0

    s = 0.5 * (f(a) + f(b))
    x = a + h
    while x <= b - h:
        s += f(x)
        x += h
    return h * s


def get_inverse_matrix(matrix):
    pass


def main():
    while True:
        print("Выберите опцию калькулятора:")
        print("1. Квадратное уравнение")
        print("2. Сумма матриц")
        print("3. Транспонирование матриц")
        print("4. Получить обратную матрцу")
        print("5. Посчитать факториал")
        print("0. Выход")

        choice = input("Введите номер опции: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()

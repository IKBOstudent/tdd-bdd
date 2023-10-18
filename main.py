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


def matrix_sum(matrix1, matrix2):
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

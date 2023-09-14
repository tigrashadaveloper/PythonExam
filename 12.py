import random

def create_matrix(rows, cols, min_value, maxvalue):
    """
    Создает матрицу с заданным числом строк и столбцов, заполняет ее случайными числами
    из заданного диапазона.
    """
    if rows != cols:
        raise ValueError("Матрица должна быть квадратной")

    matrix = []
    for _ in range(rows):
        row = [random.randint(min_value, maxvalue) for _ in range(cols)]
        matrix.append(row)

    return matrix

def calculate_average_and_count_even(matrix):
    """
    Подсчитывает среднее арифметическое элементов над главной диагональю
    и количество четных элементов под главной диагональю в матрице.
    """
    n = len(matrix)
    total_sum = 0
    count = 0
    even_count = 0

    for i in range(n):
        for j in range(n):
            if i < j:
                total_sum += matrix[i][j]
                count += 1
            elif i > j and matrix[i][j] % 2 == 0:
                even_count += 1

    if count == 0:
        average = 0
    else:
        average = total_sum / count

    return average, even_count

try:
    rows = int(input("Введите количество строк и столбцов матрицы: "))
    min_value = int(input("Введите минимальное значение элементов: "))
    max_value = int(input("Введите максимальное значение элементов: "))

    matrix = create_matrix(rows, rows, min_value, max_value)

    average, even_count = calculate_average_and_count_even(matrix)

    print("Матрица:")
    for row in matrix:
        print(row)

    print(f"Среднее арифметическое элементов над главной диагональю: {average:.2f}")
    print(f"Количество четных элементов под главной диагональю: {even_count}")

except ValueError as e:
    print(e)
except KeyboardInterrupt:
    print("Программа завершена по запросу пользователя.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

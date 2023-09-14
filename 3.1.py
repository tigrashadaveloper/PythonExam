import random


# Функция для создания случайной квадратной матрицы размера n x n
def create_random_matrix(n):
    matrix = []
    for _ in range(n):
        row = [random.randint(-100, 100) for _ in range(n)]
        matrix.append(row)
    return matrix


# Функция для вычисления среднего арифметического элементов на главной диагонали
def average_positive_main_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0
    count = 0
    for i in range(n):
        if matrix[i][i] > 0:
            diagonal_sum += matrix[i][i]
            count += 1
    if count > 0:
        return diagonal_sum / count
    else:
        return None


#Функция
#для
#вычисления
#среднего
#арифметического
#элементов
#на
#побочной
#диагонали


def average_negative_secondary_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0
    count = 0
    for i in range(n):
        if matrix[i][n - i - 1] < 0:
            diagonal_sum += matrix[i][n - i - 1]
            count += 1
    if count > 0:
        return diagonal_sum / count
    else:
        return None


#Задаем
#размер
#матрицы
n = 5  # Замените на желаемый размер матрицы

#Создаем
#случайную
#матрицу
matrix = create_random_matrix(n)

#Выводим
#матрицу
#на
#экран
print("Матрица:")
for row in matrix:
    print(row)

#Вычисляем
#средние
#значения
average_positive_main = average_positive_main_diagonal(matrix)
average_negative_secondary = average_negative_secondary_diagonal(matrix)

#Выводим
#результаты
if average_positive_main is not None:
    print(f"Среднее арифметическое положительных элементов на главной диагонали: {average_positive_main}")
else:
    print("На главной диагонали нет положительных элементов")

if average_negative_secondary is not None:
    print(f"Среднее арифметическое отрицательных элементов на побочной диагонали: {average_negative_secondary}")
else:
    print("На побочной диагонали нет отрицательных элементов")

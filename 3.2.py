import numpy as np

#Задаем размер матрицы n x n
n = 5  # Замените на необходимый размер

#Генерируем квадратную матрицу размера n x n со случайными целыми числами
matrix = np.random.randint(-10, 10, (n, n))

#Выводим матрицу на экран
print("Матрица:")
for row in matrix:
    print(row)

#Находим среднее арифметическое положительных элементов на главной диагонали
positive_elements = [matrix[i][i] for i in range(n) if matrix[i][i] > 0]
if positive_elements:
    average_positive = sum(positive_elements) / len(positive_elements)
else:
    average_positive = 0

#Находим среднее арифметическое отрицательных элементов на побочной диагонали
negative_elements = [matrix[i][n - i - 1] for i in range(n) if matrix[i][n - i - 1] < 0]
if negative_elements:
    average_negative = sum(negative_elements) / len(negative_elements)
else:
    average_negative = 0

#Выводим результаты
print(f"Среднее арифметическое положительных элементов на главной диагонали: {average_positive}")
print(f"Среднее арифметическое отрицательных элементов на побочной диагонали: {average_negative}")
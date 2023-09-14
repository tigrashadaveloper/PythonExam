import random

n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

#Генерация матрицы с случайными числами от -10 до 10
matrix = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]

#Сохранение матрицы в файл matrix.txt
with open("matrix.txt", "w") as file:
    for row in matrix:
        row_str = " ".join(map(str, row))  # Преобразование строки в текстовый формат
        file.write(row_str + "\n")

print("Матрица сохранена в файл matrix.txt.")

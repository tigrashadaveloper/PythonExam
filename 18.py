import random
import csv

#Список дней недели
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

#Запрос количества строк (n) и столбцов (m) в матрице
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

#Генерация матрицы с случайными днями недели
matrix = [[random.choice(days_of_week) for _ in range(m)] for _ in range(n)]

#Сохранение матрицы в файл matrix.csv
with open("matrix.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(matrix)

print(f"Матрица сохранена в файл matrix.csv.")
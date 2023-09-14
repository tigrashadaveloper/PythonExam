import math

#Ввод радиуса круга с клавиатуры
radius = float(input("Введите радиус круга: "))

#Вычисление площади круга
area = math.pi * radius ** 2

#Вычисление длины окружности
circumference = 2 * math.pi * radius

#Вывод результатов
print(f"Площадь круга: {area:.2f}")
print(f"Длина окружности: {circumference:.2f}")

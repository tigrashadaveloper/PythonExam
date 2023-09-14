import math

#Лямбда-функция для вычисления радиуса (R) по площади (A)
calculate_radius_from_area = lambda A: (A / math.pi) * 0.5

#Лямбда-функция для вычисления длины окружности (C) по площади (A)
calculate_circumference_from_area = lambda A: 2 * math.pi * (A / math.pi) * 0.5

#Лямбда-функция для вычисления площади (A) по радиусу (R)
calculate_area_from_radius = lambda R: math.pi * R * 2

#Лямбда-функция для вычисления площади (A) по длине окружности (C)
calculate_area_from_circumference = lambda C: (C  * 2) / (4 * math.pi)

#Примеры использования лямбда-функций
area = 25.0  # Площадь круга
radius = calculate_radius_from_area(area)
circumference = calculate_circumference_from_area(area)

print(f"Радиус круга: {radius:.2f}")
print(f"Длина окружности: {circumference:.2f}")

radius = 5.0  # Радиус круга
area = calculate_area_from_radius(radius)
circumference = calculate_circumference_from_area(area)

print(f"Площадь круга: {area:.2f}")
print(f"Длина окружности: {circumference:.2f}")
from datetime import datetime

#Функция для вычисления дня недели по дате
def get_day_of_week(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d %B %Y")
        day_of_week = date_obj.strftime("%A")
        return day_of_week
    except ValueError:
        return "Неверный формат даты"

#Примеры дат
date1 = "9 May 1945"
date2 = "12 April 1961"

#Вычисляем день недели
day_of_week1 = get_day_of_week(date1)
day_of_week2 = get_day_of_week(date2)

#Выводим результаты
print(f"День недели для {date1}: {day_of_week1}")
print(f"День недели для {date2}: {day_of_week2}")

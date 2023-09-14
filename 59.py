import math

def calculate_radius_and_area_from_circumference(circumference):
    if circumference <= 0:
        return "Ошибка: Длина окружности должна быть положительным числом."

#Вычисляем радиус круга
    radius = circumference / (2 * math.pi)

#Вычисляем площадь круга
    area = math.pi * radius ** 2

    return radius, area

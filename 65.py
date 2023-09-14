import math

def calculate_sphere_volume_from_radius_and_circumference(R, C):
    if R <= 0:
        return "Ошибка: Радиус должен быть положительным числом."
    if C <= 0:
        return "Ошибка: Длина экваториальной параллели должна быть положительным числом."

#Вычисляем объем шара
    volume = (4/3) * math.pi * R*3

    return volume

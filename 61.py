import math

#Лямбда-функция для вычисления полной поверхности цилиндра
calculate_cylinder_surface_area = lambda R, h: 2 * math.pi * R * (R + h)

#Пример использования лямбда-функции
R = 5.0  # Радиус основания цилиндра
h = 10.0  # Высота цилиндра

surface_area = calculate_cylinder_surface_area(R, h)
print(f"Полная поверхность цилиндра: {surface_area:.2f}")

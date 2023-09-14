import numpy as np
import matplotlib.pyplot as plt

#Создание списка значений x от -π до +π с шагом 0.1
x = np.arange(-np.pi, np.pi, 0.1)

#Расчет значений функций y1 = 2sin(x) и y2 = cos^2(2x)
y1 = 2 * np.sin(x)
y2 = np.cos(2 * x) ** 2

#Построение графиков функций
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y1 = 2sin(x)', color='b')
plt.plot(x, y2, label='y2 = cos^2(2x)', color='r')

#Настройка элементов графика
plt.title('Графики функций y1 и y2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

#Нахождение координат пересечения графиков
intersection_points = []

for i in range(len(x) - 1):
    if (y1[i] <= y2[i] and y1[i + 1] >= y2[i + 1]) or (y1[i] >= y2[i] and y1[i + 1] <= y2[i + 1]):
        # Используем линейную интерполяцию для приближенного определения координат пересечения
        x_intersection = x[i] + (x[i + 1] - x[i]) * (y2[i] - y1[i]) / (y1[i + 1] - y1[i])
        y_intersection = y1[i] + (y1[i + 1] - y1[i]) * (x_intersection - x[i]) / (x[i + 1] - x[i])
        intersection_points.append((x_intersection, y_intersection))

#Вывод координат пересечения
if intersection_points:
    print("Координаты точек пересечения:")
    for i, (x_inter, y_inter) in enumerate(intersection_points, 1):
        print(f"Точка {i}: x = {x_inter:.2f}, y = {y_inter:.2f}")
else:
    print("Графики не пересекаются.")

#Отображение графика
plt.show()
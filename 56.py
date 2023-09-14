import numpy as np
import matplotlib.pyplot as plt

#Создание списка значений x от -π до +π с шагом 0.1
x = np.arange(-np.pi, np.pi, 0.1)

#Вычисление значений функции y1 = 2sin(x)
y1 = 2 * np.sin(x)

#Вычисление значений функции y2 = cos^2(x)
y2 = np.cos(x) ** 2

#Построение графиков
plt.figure(figsize=(8, 6))

#График y1
plt.plot(x, y1, label='y1 = 2sin(x)', linestyle='-', color='b')

#График y2
plt.plot(x, y2, label='y2 = cos^2(x)', linestyle='--', color='r')

#Установка заголовка и подписей осей
plt.title('Графики функций y1 и y2')
plt.xlabel('x')
plt.ylabel('y')

#Добавление легенды
plt.legend()

#Включение сетки
plt.grid(True)

#Показать график
plt.show()

#Поиск приближенных координат пересечения графиков
intersection_x = x[np.abs(y1 - y2) < 0.1]
intersection_y1 = y1[np.abs(y1 - y2) < 0.1]
intersection_y2 = y2[np.abs(y1 - y2) < 0.1]

for i in range(len(intersection_x)):
    print(f"Точка пересечения {i + 1}: x = {intersection_x[i]:.2f}, y1 = {intersection_y1[i]:.2f}, y2 = {intersection_y2[i]:.2f}")

import math
import numpy as np

#Углы в градусах
угол1 = 75
угол2 = 180
угол3 = 90

#Перевод углов в радианы с использованием функции из модуля math
радианы_math1 = math.radians(угол1)
радианы_math2 = math.radians(угол2)
радианы_math3 = math.radians(угол3)

#Перевод углов в радианы с использованием функции из библиотеки numpy
радианы_numpy1 = np.deg2rad(угол1)
радианы_numpy2 = np.deg2rad(угол2)
радианы_numpy3 = np.deg2rad(угол3)

#Вывод результатов
print(f"Перевод {угол1} градусов в радианы:")
print(f"С использованием math.radians: {радианы_math1}")
print(f"С использованием numpy.deg2rad: {радианы_numpy1}")
print()

print(f"Перевод {угол2} градусов в радианы:")
print(f"С использованием math.radians: {радианы_math2}")
print(f"С использованием numpy.deg2rad: {радианы_numpy2}")
print()

print(f"Перевод {угол3} градусов в радианы:")
print(f"С использованием math.radians: {радианы_math3}")
print(f"С использованием numpy.deg2rad: {радианы_numpy3}")
print()

#Сравнение результатов
равны1 = радианы_math1 == радианы_numpy1
равны2 = радианы_math2 == радианы_numpy2
равны3 = радианы_math3 == радианы_numpy3

print("Сравнение результатов:")
print(f"Результаты для {угол1} градусов равны: {равны1}")
print(f"Результаты для {угол2} градусов равны: {равны2}")
print(f"Результаты для {угол3} градусов равны: {равны3}")

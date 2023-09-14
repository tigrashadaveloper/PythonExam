import numpy as np
import matplotlib.pyplot as plt

def Smooth(R, n):
    smoothedR = np.copy(R)  # Создаем копию входного массива
    for _ in range(5):  # Пятикратное сглаживание
        for i in range(1, n - 1):
            smoothed_R[i] = (R[i - 1] + R[i] + R[i + 1]) / 3.0  # Сглаживание значения средним арифметическим

        # Переприсваиваем сглаженные значения обратно в R
        R[:] = smoothed_R

        # Выводим результат сглаживания в виде массива
        print(f"Сглаживание {len(R)} элементов: {R}")

        # Строим график
        plt.plot(range(len(R)), R)
        plt.xlabel('Индекс')
        plt.ylabel('Значение')
        plt.title(f"Сглаживание {len(R)} элементов")
        plt.show()

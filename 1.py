import numpy as np

def find_closest_points(x, y):
    min_distance = None
    closest_points = None

    for i in range(len(x)):
        for j in range(len(y)):
            distance = np.linalg.norm(x[i] - y[j])
            if min_distance is None or distance < min_distance:
                min_distance = distance
                closest_points = (x[i], y[j])

    return closest_points, min_distance

n = 3  # Замените на необходимую размерность векторов
x = np.random.randint(0, 100, (n,))  # Генерируем случайные векторы x и y
y = np.random.randint(0, 100, (n,))

closest_points, min_distance = find_closest_points(x, y)
print("Наиболее близкие точки:", closest_points)
print("Минимальное расстояние:", min_distance)

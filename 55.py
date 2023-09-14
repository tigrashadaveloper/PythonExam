import math

def calculate_ring_area(R1, R2):
    if R1 >= R2:
        ring_area = math.pi * (R1  - R2  )
        return ring_area
    else:
        return "Ошибка: Внешний радиус (R1) должен быть больше или равен внутреннему радиусу (R2)."

#Пример использования функции
R1 = 10.0  # Внешний радиус
R2 = 5.0   # Внутренний радиус

ring_area = calculate_ring_area(R1, R2)
if isinstance(ring_area, float):
    print(f"Площадь кольца с внешним радиусом {R1} и внутренним радиусом {R2} равна {ring_area:.2f}")
else:
    print(ring_area)

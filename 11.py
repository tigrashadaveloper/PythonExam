from functools import reduce

def double_factorial(n):
    if n <= 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(n, 0, -2))

n = 7  # Замените на желаемое натуральное число
result = double_factorial(n)
print(f"Двойной факториал числа {n} равен {result}")

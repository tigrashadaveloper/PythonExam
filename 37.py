def сложениеположительных(a, b):
    # Проверяем, что a и b положительные числа
    assert a >= 0 and b >= 0, "Введены отрицательные числа"

#Выполняем сложение
    результат = a + b

    return результат

#Пример использования функции
try:
    число1 = int(input("Введите первое положительное число: "))
    число2 = int(input("Введите второе положительное число: "))

    результатсложения = сложениеположительных(число1, число2)
    print(f"Результат сложения: {результатсложения}")
except AssertionError as e:
    print(f"Ошибка: {e}")
except ValueError:
    print("Введите корректные числа")

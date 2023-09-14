import inspect

def func(fn):
    # Получаем имя функции
    имяфункции = fn.name

    # Получаем сигнатуру функции (информацию о параметрах)
    сигнатура = inspect.signature(fn)

    # Извлекаем информацию о параметрах
    параметры = сигнатура.parameters

    информация = []

    for имя, параметр in параметры.items():
        тип = параметр.annotation if параметр.annotation != inspect.Parameter.empty else None

        if параметр.default == inspect.Parameter.empty:
            информация.append(f"{имя} - позиционный{' ' + str(тип) if тип else ''}")
        else:
            информация.append(f"{имя} - ключевой{' ' + str(тип) if тип else ''}")

    # Выводим информацию
    print(f"Имя функции: {имяфункции}")
    for строка in информация:
        print(строка)

#Пример использования функции
def subfunc(a: int, b: float):
    pass

func(subfunc)

def выдачаденег(сумма):
    номиналы = [500, 100, 10, 1]
    количестводенег = [0, 0, 0, 0]

    for номинал in номиналы:
        количестводенег[номиналы.index(номинал)] = сумма // номинал
        сумма %= номинал

    return количестводенег

#Пример использования функции
сумма = 3875
количестводенег = выдачаденег(сумма)

print(f"Количество купюр по 500 рублей: {количестводенег[0]}")
print(f"Количество купюр по 100 рублей: {количестводенег[1]}")
print(f"Количество купюр по 10 рублей: {количестводенег[2]}")
print(f"Количество монет по 1 рублю: {количестводенег[3]}")
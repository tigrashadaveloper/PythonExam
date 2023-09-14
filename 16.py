import random

# Функция для генерации n действительных чисел в заданном диапазоне и записи их в файл
def generate_numbers(filename, n, min_value, max_value):
    numbers = [random.uniform(min_value, max_value) for _ in range(n)]
    with open(filename, "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

# Функция для чтения чисел из файла и вывода их на консоль
def read_numbers(filename):
    try:
        with open(filename, "r") as file:
            numbers = [float(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print("Файл не найден.")
        return []

# Функция для выполнения операций над числами из файла и вывода результатов
def perform_operations(numbers):
    if not numbers:
        return

    # 1. Вычислить сумму и произведение всех чисел
    sum_numbers = sum(numbers)
    product_numbers = 1
    for number in numbers:
        product_numbers *= number

    # 2. Найти наибольшее и наименьшее число
    max_number = max(numbers)
    min_number = min(numbers)

    # 3. Вычислить сумму положительных чисел
    positive_numbers_sum = sum(number for number in numbers if number > 0)

    # 4. Вычислить сумму отрицательных чисел
    negative_numbers_sum = sum(number for number in numbers if number < 0)

    # Вывод результатов
    print(f"Сумма всех чисел: {sum_numbers}")
    print(f"Произведение всех чисел: {product_numbers}")
    print(f"Наибольшее число: {max_number}")
    print(f"Наименьшее число: {min_number}")
    print(f"Сумма положительных чисел: {positive_numbers_sum}")
    print(f"Сумма отрицательных чисел: {negative_numbers_sum}")

# Главная программа
while True:
    print("\nВыберите режим работы:")
    print("1. Генерация и запись чисел в файл")
    print("2. Чтение чисел из файла и вывод на консоль")
    print("3. Выполнение операций над числами из файла и вывод результатов")
    print("4. Выход")
    choice = input("Введите номер режима (1/2/3/4): ")

    if choice == "1":
        n = int(input("Введите количество чисел: "))
        min_value = float(input("Введите минимальное значение: "))
        max_value = float(input("Введите максимальное значение: "))
        filename = input("Введите имя файла для записи: ")
        generate_numbers(filename, n, min_value, max_value)
        print(f"{n} чисел записано в файл {filename}")

    elif choice == "2":
        filename = input("Введите имя файла для чтения: ")
        numbers = read_numbers(filename)
        if numbers:
            print("Числа из файла:")
            for number in numbers:
                print(number)

    elif choice == "3":
        filename = input("Введите имя файла для выполнения операций: ")
        numbers = read_numbers(filename)
        if numbers:
            perform_operations(numbers)

    elif choice == "4":
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите существующий режим (1/2/3/4).")
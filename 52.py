# Функция для поиска цены товара
def find_price(product_name, file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, price = line.strip().split(': ')
                if name == product_name:
                    return float(price)
            return "Цена не известна"
    except FileNotFoundError:
        return "Файл не найден"

# Функция для добавления новых товаров
def add_products(new_products, file_name):
    try:
        with open(file_name, 'a') as file:
            for product in new_products:
                file.write(product + '\n')
    except FileNotFoundError:
        return "Файл не найден"

# Функция для удаления информации о товаре
def remove_product(product_name, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        with open(file_name, 'w') as file:
            for line in lines:
                name, _ = line.strip().split(': ')
                if name != product_name:
                    file.write(line)
    except FileNotFoundError:
        return "Файл не найден"

# Функция для создания нового файла с сортированными товарами
def create_sorted_file(input_file_name, output_file_name):
    try:
        with open(input_file_name, 'r') as file:
            lines = file.readlines()
        sorted_lines = sorted(lines, key=lambda line: float(line.strip().split(': ')[1]))
        with open(output_file_name, 'w') as file:
            file.writelines(sorted_lines)
    except FileNotFoundError:
        return "Файл не найден"

# Создание исходного файла с товарами
file_name = "products.txt"
initial_products = ["Товар1: 100.0", "Товар2: 150.0", "Товар3: 80.0"]
with open(file_name, 'w') as file:
    file.writelines('\n'.join(initial_products))

# Вывод цены указанного товара
product_name_to_find = "Товар1"
result = find_price(product_name_to_find, file_name)
print("Цена товара:", result)

# Добавление новых товаров
new_products_to_add = ["Товар4: 120.0", "Товар5: 75.0", "Товар6: 200.0"]
add_products(new_products_to_add, file_name)

# Удаление товара
product_to_remove = "Товар3"
remove_product(product_to_remove, file_name)

# Создание нового файла с сортировкой
sorted_file_name = "sorted_products.txt"
create_sorted_file(file_name, sorted_file_name)

# Вывод информации о двух самых дешевых и двух самых дорогих товарах
with open(sorted_file_name, 'r') as file:
    all_lines = file.readlines()
    cheapest = all_lines[:2]
    most_expensive = all_lines[-2:]
    print("Две самых дешевых товара:")
    for line in cheapest:
        print(line.strip())
    print("Две самых дорогих товара:")
    for line in most_expensive:
        print(line.strip())

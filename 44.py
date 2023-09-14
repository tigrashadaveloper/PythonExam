import csv

def find_by_name(file_name, names):
    # Создаем пустой список для хранения найденных данных
    result = []

    # Открываем CSV-файл для чтения
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)

#Проходимся по каждой строке в файле
        for row in csvreader:
            # Проверяем, содержится ли имя из текущей строки в переданных именах
            if row['First Name'] in names:
                result.append(row)

    return result

#Пример использования функции
file_name = 'example.csv'  # Замените на имя вашего CSV-файла
names_to_find = ['John', 'Alice']
found_data = find_by_name(file_name,names_to_find)

#Выводим найденные данные
for data in found_data:
    print(data)

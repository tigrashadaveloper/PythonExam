#Открываем файл для чтения
with open('имя_файла.txt', 'r') as файл:
    # Счетчик вхождений символа "!"
    счетчик = 0

#Читаем файл построчно
    for строка in файл:
        # Проверяем, содержит ли строка символ "!"
        if '!' in строка:
            счетчик += строка.count('!')
            print(строка.strip())  # Выводим строку без лишних пробелов и символов перевода строки

#Выводим количество вхождений символа "!"
print(f"Количество вхождений символа '!': {счетчик}")

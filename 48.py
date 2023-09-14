evgene_o = """My uncle -- high ideals inspire him;
 but when past joking he fell sick,
 he really forced one to admire him --
 and never played a shrewder trick.
 Let others learn from his example!
 But God, how deadly dull to sample
 sickroom attendance night and day
 and never stir a foot away!
 And the sly baseness, fit to throttle,
 of entertaining the half-dead:
 one smoothes the pillows down in bed,
 and glumly serves the medicine bottle,
 and sighs, and asks oneself all through:
 When will the devil come for you? """

#Создаем пустой словарь для подсчета символов
character_count = {}

#Перебираем символы в строке и обновляем словарь
for char in evgene_o:
    # Игнорируем пробелы и знаки пунктуации
    if char.isalnum():
        # Если символ уже есть в словаре, увеличиваем его счетчик
        if char in character_count:
            character_count[char] += 1
        else:
            # Если символа нет в словаре, добавляем его с начальным счетчиком 1
            character_count[char] = 1

# счетчик строчных букв
lowercase_count = 0

#Перебираем символы в словаре и проверяем, являются ли они строчными буквами
for char in character_count:
    if char.islower():
        lowercase_count += character_count[char]

#Выводим результаты
print("Словарь с количеством символов:")
print(character_count)
print("Количество строчных букв в строке evgene_o:", lowercase_count)

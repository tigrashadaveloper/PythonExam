sentence = "Пример предложения с несколькими словами"

#Разделяем предложение на слова по пробелам
words = sentence.split()

#Генерируем список из первых букв каждого слова
first_letters = [word[0] for word in words]

#Соединяем буквы в слово
result_word = ''.join(first_letters)

#Выводим результат
print("Слово из первых букв:", result_word)

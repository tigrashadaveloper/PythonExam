def repl(input_str, **kwargs):
    # Разбиваем входную строку на слова
    words = input_str.split()

#Проходим по каждому слову и, если оно является именем параметра, заменяем его на значение параметра
    for i in range(len(words)):
        word = words[i]
        if word in kwargs:
            words[i] = kwargs[word]

#Собираем измененные слова обратно в строку
    result_str = ' '.join(words)

    return result_str

#Пример использования
input_str = 'replace my val abc'
result = repl(input_str, my='s1', abc='fff')
print(result)  # Вывод: 'replace s1 val fff'

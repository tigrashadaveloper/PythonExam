def count_letter_in_word(word, letter):
    """
    Функция для подсчета количества заданной буквы в слове.
    """
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

def total_letter_count(words, letter):
    """
    Функция для подсчета общего количества заданной буквы в списке слов.
    """
    total_count = 0
    for word in words:
        total_count += count_letter_in_word(word, letter)
    return total_count

#Пример использования
words = ["apple", "banana", "cherry", "date"]
letter_to_count = "a"
total_count = total_letter_count(words, letter_to_count)
print(f"Общее количество букв '{letter_to_count}' в словах: {total_count}")

def calculate_letter_percentage(word, letter):
    """
    Функция для расчета доли заданной буквы в слове (в процентах).
    """
    total_chars = len(word)
    if total_chars == 0:
        return 0.0  # Избегаем деления на ноль
    letter_count = word.count(letter)
    return (letter_count / total_chars) * 100.0

def find_word_with_highest_percentage(words, letter):
    """
    Функция для нахождения слова с наибольшей долей заданной буквы в списке слов.
    """
    max_percentage = 0
    word_with_highest_percentage = None
    for word in words:
        percentage = calculate_letter_percentage(word, letter)
        if percentage > max_percentage:
            max_percentage = percentage
            word_with_highest_percentage = word
    return word_with_highest_percentage, max_percentage

#Пример использования
words = ["apple", "banana", "cherry", "date"]
letter_to_check = "a"
word, percentage = find_word_with_highest_percentage(words, letter_to_check)
print(f"Слово с наибольшей долей буквы '{letter_to_check}' это '{word}' с долей {percentage:.2f}%")

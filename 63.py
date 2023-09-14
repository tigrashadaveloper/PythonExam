from datetime import datetime

#Введите дату рождения в формате ГГГГ-ММ-ДД
birthdate = input("Введите дату рождения (ГГГГ-ММ-ДД): ")

try:
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    current_date = datetime.now()

#Вычисляем разницу между текущей датой и датой рождения
    delta = current_date - birthdate

#Получаем количество прожитых дней
    days_lived = delta.days

    print(f"Количество прожитых дней: {days_lived} дней")
except ValueError:
    print("Ошибка: Некорректный формат даты. Введите дату в формате ГГГГ-ММ-ДД.")

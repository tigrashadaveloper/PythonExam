from datetime import datetime

#Функция для вычисления дня недели по дате
def get_day_of_week(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d %B %Y")
        day_of_week = date_obj.strftime("%A")
        return day_of_week
    except ValueError:
        return "Неверный формат даты"

#Примеры дат
date1 = "9 May 1945"
date2 = "12 April 1961"

#Вычисляем день недели
day_of_week1 = get_day_of_week(date1)
day_of_week2 = get_day_of_week(date2)

#Выводим результаты
print(f"День недели для {date1}: {day_of_week1}")
print(f"День недели для {date2}: {day_of_week2}")

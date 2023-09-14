from datetime import datetime

def count_day(start_date, end_date):
    # Преобразуем строки с датами в объекты datetime
    start_date = datetime.strptime(start_date, '%d.%m.%Y')
    end_date = datetime.strptime(end_date, '%d.%m.%Y')

    # Вычисляем разницу между датами
    delta = end_date - start_date

    # Извлекаем количество дней из разницы
    return delta.days

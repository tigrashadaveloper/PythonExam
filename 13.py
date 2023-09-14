try:
    import datetime  # Попытка импортировать модуль datetime
except ImportError:
    print("Ошибка: Не удалось импортировать модуль datetime.")
else:
    try:
        now = datetime.datetime.now()  # Попытка получить текущее время и дату
        print(f"Текущая дата и время: {now}")
    except Exception as e:
        print(f"Произошла ошибка при работе с datetime: {e}")

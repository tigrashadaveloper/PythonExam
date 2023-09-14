#Создаем список результатов группы
group_results = [
    ["Иванов", 4, 3, 5],   # Фамилия, История, Математика, Информатика
    ["Петров", 5, 2, 4],
    ["Сидоров", 3, 3, 2],
    ["Смирнов", 0, 5, 4],
    ["Козлов", 2, 4, 3],
]

#a) Выводим таблицу с результатами экзаменов
print("a) Таблица с результатами экзаменов:")
print("Фамилия\tИстория\tМатематика\tИнформатика")
for student in group_results:
    print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}")

#b) Выводим фамилии студентов с задолженностями и названия несданных предметов
print("\nb) Студенты с задолженностями:")
for student in group_results:
    if 0 in student[1:]:
        subjects_with_failures = []
        if student[1] == 0:
            subjects_with_failures.append("История")
        if student[2] == 0:
            subjects_with_failures.append("Математика")
        if student[3] == 0:
            subjects_with_failures.append("Информатика")
        print(f"{student[0]} задолжал по {', '.join(subjects_with_failures)}")

#c) Считаем количество оценок по дисциплине Информатика
grades_in_informatics = {
    "Неявка": 0,
    "Неудовлетворительно": 0,
    "Удовлетворительно": 0,
    "Хорошо": 0,
    "Отлично": 0,
}

for student in group_results:
    informatics_grade = student[3]
    if informatics_grade == 0:
        grades_in_informatics["Неявка"] += 1
    elif informatics_grade == 2:
        grades_in_informatics["Неудовлетворительно"] += 1
    elif informatics_grade == 3:
        grades_in_informatics["Удовлетворительно"] += 1
    elif informatics_grade == 4:
        grades_in_informatics["Хорошо"] += 1
    elif informatics_grade == 5:
        grades_in_informatics["Отлично"] += 1

print("\nc) Количество оценок по дисциплине Информатика:")
for grade, count in grades_in_informatics.items():
    print(f"{grade}: {count}")

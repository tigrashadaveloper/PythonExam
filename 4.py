#Создаем словарь с результатами группы
group_results = {
    "Студент1": [4, 3, 5],  # Фамилия студента: [История, Математика, Информатика]
    "Студент2": [5, 2, 4],
    "Студент3": [3, 3, 2],
    "Студент4": [0, 5, 4],
    "Студент5": [2, 4, 3],
}

#a) Выводим таблицу с результатами экзаменов
print("a) Таблица с результатами экзаменов:")
print("Фамилия\tИстория\tМатематика\tИнформатика")
for student, grades in group_results.items():
    print(f"{student}\t{grades[0]}\t{grades[1]}\t{grades[2]}")

#b) Вычисляем средний балл по каждой дисциплине
num_students = len(group_results)
num_exams = len(next(iter(group_results.values())))
average_grades = [0] * num_exams

for student, grades in group_results.items():
    for i in range(num_exams):
        average_grades[i] += grades[i]

for i in range(num_exams):
    average_grades[i] /= num_students

print("\nb) Средний балл по каждой дисциплине:")
print("История:", average_grades[0])
print("Математика:", average_grades[1])
print("Информатика:", average_grades[2])

#c) Вычисляем средний балл для каждого студента и выводим результат
print("\nc) Средний балл для каждого студента:")
for student, grades in group_results.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student}: {average_grade}")

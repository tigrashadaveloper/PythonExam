#Чтение из файла f.txt и запись в файл g.txt
with open("f.txt", "r") as f, open("g.txt", "w") as g:
    for line in f:
        number = int(line.strip())
        if number % 2 != 0:
            g.write(str(number) + "\n")

#Чтение из файла f.txt и запись нечетных чисел в файл h.txt
with open("f.txt", "r") as f, open("h.txt", "w") as h:
    for line in f:
        number = int(line.strip())
        if number % 2 == 0:
            h.write(str(number) + "\n")

#Добавление содержимого файла h.txt в файл g.txt
with open("h.txt", "r") as h, open("g.txt", "a") as g:
    for line in h:
        g.write(line)

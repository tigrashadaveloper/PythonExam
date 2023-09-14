def argk3(*, var1=None, var2=None, var3=None):
    переданныеаргументы = []

    if var1 is not None:
        переданныеаргументы.append(f"var1 = {var1}")

    if var2 is not None:
        переданныеаргументы.append(f"var2 = {var2}")

    if var3 is not None:
        переданныеаргументы.append(f"var3 = {var3}")

    if переданныеаргументы:
        сообщение = "Переданы аргументы: " + ", ".join(переданныеаргументы)
        print(сообщение)
    else:
        print("Аргументы не переданы.")

#Примеры использования функции
argk3(var1=2, var3=10)
argk3(var2="Hello")
argk3()

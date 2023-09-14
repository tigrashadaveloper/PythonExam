def arg_k3p3(arg1, arg2, arg3, /, *, var1=None, var2=None, var3=None):
    print(f"Позиционные аргументы: {arg1}, {arg2}, {arg3}")
    print(f"Ключевые аргументы: var1={var1}, var2={var2}, var3={var3}")

#Примеры использования функции
arg_k3p3(1, 2, 3, var1="A", var2="B", var3="C")
arg_k3p3(10, 20, 30)

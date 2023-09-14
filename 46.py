import re
from fractions import Fraction

#Функция для преобразования дробей из строки в Fraction
def parse_fraction(fraction_str):
    # Разбиваем строку на целую часть и дробную часть (если она есть)
    parts = re.split(r'\s+', fraction_str)

#Если есть только одна часть, это целое число
    if len(parts) == 1:
        return Fraction(int(parts[0]))

#Если есть две части, это смешанная дробь
    if len(parts) == 2:
        whole_part = int(parts[0])
        fractional_part = Fraction(parts[1])
        return whole_part + fractional_part

#Если есть три части, это правильная дробь
    if len(parts) == 3:
        whole_part = int(parts[0])
        numerator = int(parts[1])
        denominator = int(parts[2])
        return whole_part + Fraction(numerator, denominator)

#Функция для выполнения операции сложения
def add_fractions(expression):
    operands = expression.split('+')
    result = sum(map(parse_fraction, operands))
    return result

#Функция для выполнения операции умножения
def multiply_fractions(expression):
    operands = expression.split('')
    result = 1
    for operand in operands:
        result= parse_fraction(operand)
    return result

#Ваш входной пример
expression1 = "1 3/5 + 2/3"
result1 = add_fractions(expression1)
print(result1)  # Выведет 2 4/15

expression2 = "2/9 * 6/5"
result2 = multiply_fractions(expression2)
print(result2)  # Выведет 4/15

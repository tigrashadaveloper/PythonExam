def расчетподоходногоналога(оклад, ставканалога):
    # Расчет размера подоходного налога
    налог = (оклад * ставканалога) / 100

#Расчет суммы, получаемой на руки
    сумма = оклад - налог

    return налог, сумма

#Пример использования функции
оклад = 50000  # Замените на ваш оклад
ставканалога = 15  # Замените на вашу ставку подоходного налога

налог, сумма = расчетподоходногоналога(оклад, ставканалога)

print(f"Размер подоходного налога: {налог} руб.")
print(f"Сумма, получаемая на руки: {сумма} руб.")

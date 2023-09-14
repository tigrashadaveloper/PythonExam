class Заказ:
    def init(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def str(self):
        return f"Товар {self.code}, цена {self.price} руб., количество {self.count} шт."

class Опт(Заказ):
    def init(self, code, price, count):
        super().init(code, price, count)

    def summa(self):
        if self.count > 500:
            return self.price * self.count * 0.90
        else:
            return self.price * self.count * 0.95

    def str(self):
        return f"Оптовый заказ: {super().str()}, стоимость {self.summa()} руб."

class Розница(Заказ):
    def init(self, code, price, count):
        super().init(code, price, count)

    def summa(self):
        return self.price * self.count

    def str(self):
        return f"Розничный заказ: {super().str()}, стоимость {self.summa()} руб."

#Примеры использования классов
оптовыйзаказ = Опт("Товар1", 100, 600)
розничныйзаказ = Розница("Товар2", 150, 10)

print(оптовыйзаказ)
print(розничныйзаказ)


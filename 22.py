class Интервалы:
    def __init__(self, левая_граница, правая_граница):
        self.левая_граница = левая_граница
        self.правая_граница = правая_граница

    def длина_интервала(self):
        return self.правая_граница - self.левая_граница

    def смещение_влево(self, сдвиг):
        self.левая_граница -= сдвиг
        self.правая_граница -= сдвиг

    def смещение_вправо(self, сдвиг):
        self.левая_граница += сдвиг
        self.правая_граница += сдвиг

    def сжатие_интервала(self, коэффициент):
        центр = (self.левая_граница + self.правая_граница) / 2
        полудлина = self.длина_интервала() / 2
        новая_полудлина = полудлина / коэффициент
        self.левая_граница = центр - новая_полудлина
        self.правая_граница = центр + новая_полудлина

    def сравнение(self, другой_интервал):
        if self.правая_граница < другой_интервал.левая_граница:
            return "Интервал 1 левее интервала 2"
        elif self.левая_граница > другой_интервал.правая_граница:
            return "Интервал 1 правее интервала 2"
        else:
            return "Интервалы пересекаются"

    def сумма(self, другой_интервал):
        левая_граница = self.левая_граница + другой_интервал.левая_граница
        правая_граница = self.правая_граница + другой_интервал.правая_граница
        return Интервалы(левая_граница, правая_граница)

    def разность(self, другой_интервал):
        левая_граница = self.левая_граница - другой_интервал.правая_граница
        правая_граница = self.правая_граница - другой_интервал.левая_граница
        return Интервалы(левая_граница, правая_граница)

    def __str__(self):
        return f"[{self.левая_граница}, {self.правая_граница}]"


# Пример использования класса
интервал1 = Интервалы(2, 6)
интервал2 = Интервалы(4, 8)

print(f"Длина интервала 1: {интервал1.длина_интервала()}")
print(f"Сравнение интервалов: {интервал1.сравнение(интервал2)}")

интервал1.смещение_вправо(2)
print(f"Интервал 1 после смещения вправо: {интервал1}")

интервал2.сжатие_интервала(2)
print(f"Интервал 2 после сжатия: {интервал2}")

сумма = интервал1.сумма(интервал2)
разность = интервал1.разность(интервал2)

print(f"Сумма интервалов: {сумма}")
print(f"Разность интервалов: {разность}")
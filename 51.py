class Length:
    def init(self, value, unit='м'):
        self.value = value
        self.unit = unit
        self.valid_units = {'см': 0.01, 'м': 1.0, 'км': 1000.0}

    @property
    def unit(self):
        return self.unit

    @unit.setter
    def unit(self, new_unit):
        if new_unit in self.valid_units:
            self.value *= self.valid_units[new_unit] / self.valid_units[self.unit]
            self.unit = new_unit
        else:
            raise ValueError("Недопустимая единица измерения. Допустимые значения: 'см', 'м', 'км'")

    def str__(self):
        return f"{self.value} {self.unit}"

#Примеры использования класса
length1 = Length(100, 'см')
print(length1)  # Выведет "100 см"

length2 = Length(2, 'м')
print(length2)  # Выведет "2 м"

length2.unit = 'км'
print(length2)  # Выведет "0.002 км"

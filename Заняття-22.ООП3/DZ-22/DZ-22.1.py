# Створити клас Лінійка яка при створенні задаємо довжину
# Опишіть магічного методу __str__
# який буде повертати текст в форматі “<Лінійка на 20см>”
# а також опишіть метод __add__
# Для операції додавання (додавати довжину лінійки через оператор “+”)


class Line:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return "<Лінійка на {} см".format(self.length)

    def __add__(self, new_line):
        if isinstance(new_line, Line):
            new_length = self.length + new_line.length
            return Line(new_length)
        else:
            raise TypeError("Розмір тільки цифрами")


Line1 = Line(20)
Line2 = Line(30)

print(Line1)
print(Line2)

Line3 = Line1 + Line2

print(Line3)
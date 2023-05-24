# Створіть клас Автомобіль
# в якого  колір одразу заданий наприклад зелений
# створити методи класу set_red_default
# (@classmethod) – який змінить всім обєктам колір на червоний

class Auto:
    color_default = " Зелений"

    def __init__(self, color):
        self.color = color

    @classmethod
    def set_red_color_default(cls):
        cls.color_default = "Червоний"

    def __str__(self):
        return f"Автомобіль кольору: {self.color}"

    def set_default_color(self):
        self.color = self.color_default


Auto1 = Auto("Зелений")
Auto2 = Auto("Синій")

print(Auto1)
print(Auto2)

Auto.set_red_color_default()

Auto1.set_default_color()
Auto2.set_default_color()

print(Auto1)
print(Auto2)


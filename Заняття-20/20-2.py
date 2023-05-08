# Завдання 4
# Створіть клас «Дріб». Збережіть у класі чисельник та знаменник.
# Реалізуйте методи класу для введення-виведення даних.
# Також створіть методи класу для виконання арифметичних операцій
# (додавання, віднімання, множення, ділення і т. д.)


class drib:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def display_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

    def update_fraction(self):
        self.numerator = int(input("Введіть чисельник: "))
        self.denominator = int(input("Введіть знаменник : "))

    def add_fraction(self, other_fraction):
        common_denominator = self.denominator * other_fraction.denominator
        common_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        return drib(common_numerator, common_denominator)

    def subtract_fraction(self, other_fraction):
        common_denominator = self.denominator * other_fraction.denominator
        common_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        return drib(common_numerator, common_denominator)

    def multiply_fraction(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return drib(new_numerator, new_denominator)

    def divide_fraction(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return drib(new_numerator, new_denominator)

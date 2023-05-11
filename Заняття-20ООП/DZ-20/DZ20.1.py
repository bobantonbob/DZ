# Завдання 1
# Реалізуйте клас «Автомобіль».
# Збережіть у класі: назву моделі, рік випуску, виробника,
# об’єм двигуна, колір машини, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Car:
    def __init__(self, model_name, graduation_year, producer, engine_capacity, color, price):
        self.model_name = model_name
        self.graduation_year = graduation_year
        self.producer = producer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def get_model_name(self):
        return self.model_name

    def get_graduation_year(self):
        return self.graduation_year

    def get_producer(self):
        return self.producer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


    def set_model_name(self, model_name):
        self.model_name = model_name

    def set_graduation_year(self, graduation_year):
        self.graduation_year = graduation_year

    def set_producer(self, producer):
        self.producer = producer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


    def display_info(self):
        print(f"Назва авто : {self.model_name}")
        print(f"Рік випуску : {self.graduation_year}")
        print(f"Виробник : {self.producer}")
        print(f"Об'єм двигуна : {self.engine_capacity}")
        print(f"Колір машини : {self.color}")
        print(f"Ціна авто : {self.price}")

    def update_info(self):
        self.model_name = input("Назва авто :")
        self.graduation_year = input("Рік випуску :")
        self.producer = input("Виробник :")
        self.engine_capacity = input("Об'єм двигуна :")
        self.color = input("Колір машини :")
        self.price = input("Ціна авто :")


audi = Car("Audi", 2000, "Germany", 2000, "red", 22000)

print(audi.model_name)
print(audi.graduation_year)
print(audi.producer)
print(audi.engine_capacity)
print(audi.color)
print(audi.price)


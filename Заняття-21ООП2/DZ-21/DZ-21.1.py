# Створіть клас Device, який містить інформацію про пристрій
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine,
# Клас Blender
# Клас MeatGrinder.
# Кожен із класів має містити необхідні для роботи методи.


class Device:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

class CoffeeMachine(Device):
    def __init__(self, name, brand, price):
        super().__init__(name, brand, price)
        self.milk_liters = 0
        self.water_liters = 0

    def add_water(self, amount):
        self.water_liters += amount
        print(f"До кавимашини {self.brand} {self.name} додано {amount} мл. води. ")


    def add_milk(self, amount):
        self.milk_liters += amount
        print(f"До кавимашини {self.brand} {self.name} додано {amount} мл. молока. ")

    def make_coffee(self):
        if self.water_liters >= 200 and self.milk_liters >= 100:
            print(f"Кавомашина {self.brand} {self.name} робить лате. ")
            self.water_liters -= 200
            self.milk_liters -= 100
        else:
            print("Перевірте рівень води та молока")


class Blender(Device):
    def __init__(self, name, brand, price):
        super().__init__(name, brand, price)
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        print(f"Блендер {self.brand} {self.name} встановили на {self.speed} обертів. ")

    def blend(self):
        if self.speed > 0:
            print(f"Бленде {self.brand} {self.name} змішує. ")
        else:
            print("Вкажіть швидкість для зміщування. ")

class MeatGrinder(Device):
    def __init__(self, name, brand, price):
        super().__init__(name, brand, price)
        self.power = False
    def power_switch(self):
        if self.power:
            self.power = False
            print(f"Мясорубка {self.brand} {self.name} виключина. ")
        else:
            self.power = True
            print(f"Мясорубка {self.brand} {self.name} включена. ")

    def grinding(self):
        if self.power:
            print(f"Мясорубка {self.brand} {self.name} перемелює м'ясо. ")
        else:
            print("Будь ласка включить мясорубку. ")


coffee_machine = CoffeeMachine("H150","Philips", 2020)
coffee_machine.add_milk(600)
coffee_machine.add_water(600)
coffee_machine.make_coffee()
print("\033[35mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \033[0m")
blender = Blender("ZQ125", "Braun", 2500)
blender.set_speed(12)
blender.blend()
print("\033[35mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \033[0m")

meat_grinder = MeatGrinder('QW250', "Goren", 3050)
meat_grinder.power_switch()
meat_grinder.grinding()



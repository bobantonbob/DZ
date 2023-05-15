# Створіть клас Passport, який міститеме паспортну інформацію про громадянина заданої країни
# За допомогою механізму успадкування реалізуйте клас ForeingPassport, похідний від Passport
# Нагадаймо, ща закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного паспорта.
# Кожен із класів має містити необхідні методи.

class Passport:
    def __init__(self, name, passport_number, nationality):
        self.name = name
        self.passport_number = passport_number
        self.nationality = nationality

    def display_info(self):
        print(f"Паспортні дані :")
        print(f"ІПН громадянина : {self.name}")
        print(f"Номер паспорту: {self.passport_number}")
        print(f"Громадянство: {self.nationality}")

class ForeignPassport(Passport):
    def __init__(self, name, passport_number, nationality):
        super().__init__(name, passport_number, nationality)
        self.visas = []
        self.foreign_passport_number = ""

    def add_visa(self, visa):
        self.visas.append(visa)
        print(f"Добавити візу : {visa}")

    def set_foreign_passport_number(self, passport_number):
        self.foreign_passport_number = passport_number
        print(f"Номер закордонного паспорта : {passport_number}")

    def display_info(self):
        super().display_info()
        print(f"Дані закордонного паспорта:")
        print(f"Номер закордонного паспорта: {self.foreign_passport_number}")
        print(f"Віза: {', '.join(self.visas)}")

print("\033[35mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \033[0m")
passport = Passport("Бабенко Антон Іванович", "АА234589ИИ", "UA")
passport.display_info()
print("\033[35mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \033[0m")

foreign_passport = ForeignPassport("Іванов Антон Іванович", "B9876543", "Germany")
foreign_passport.add_visa("France")
foreign_passport.add_visa("USA")
foreign_passport.set_foreign_passport_number("Z54321")
print("\033[35mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \033[0m")
foreign_passport.display_info()
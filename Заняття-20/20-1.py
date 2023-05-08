# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ, дату народження,
# контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class human:
    def __init__(self, full_name, birth_date, phone, city, country, address):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def get_full_name(self):
        return self.full_name

    def get_birth_date(self):
        return self.birth_date

    def get_phone_number(self):
        return self.phone

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_home_address(self):
        return self.address

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_phone_number(self, phone_number):
        self.phone = phone

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country

    def set_home_address(self, address):
        self.address = address

    def display_info(self):
        print(f"ПІБ: {self.full_name}")
        print(f"Дата народження: {self.birth_date}")
        print(f"Контактний телефон: {self.phone}")
        print(f"Місто: {self.city}")
        print(f"Країна: {self.country}")
        print(f"Домашня адреса: {self.address}")

    def update_info(self):
        self.full_name = input("ПІБ : ")
        self.birth_date = input("Дата народження : ")
        self.phone_number = input("Контактний телефон: ")
        self.city = input("Місто: ")
        self.country = input("Країна: ")
        self.home_address = input("Домашня адреса: ")


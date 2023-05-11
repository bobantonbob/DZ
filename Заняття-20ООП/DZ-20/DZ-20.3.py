# Завдання 3
# Реалізуйте клас «Стадіон».
# Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.


class Stadium:
    def __init__(self, name_stadium, opening_date, country, city, capacity):
        self.name_stadium = name_stadium
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print("Назва стадіону :", self.name_stadium)
        print("Дата відкриття :", self.opening_date)
        print("Країна :", self.country)
        print("Місто :", self.city)
        print("Місткість:", self.capacity)

    def set_name_stadium(self, new_name_stadium):
        self.name_stadium = new_name_stadium

    def get_name_stadium(self):
        return self.name_stadium


    def set_opening_date(self, new_opening_date):
        self.opening_date = new_opening_date

    def get_opening_date(self):
        return self.name_book


    def set_country(self, new_country):
        self.country = new_country

    def get_country(self):
        return self.country


    def set_city(self, new_city):
        self.city = new_city

    def get_city(self):
        return self.city


    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def get_capacity(self):
        return self.capacity



# Завдання 2
# Реалізуйте клас «Книга».
# Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.


class Book:
    def __init__(self, name_book, year_publication, publisher, genre, author, price):
        self.name_book = name_book
        self.year_publication = year_publication
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print("Назва книги:", self.name_book)
        print("Рік видання:", self.year_publication)
        print("Видавець:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Ціна:", self.price)

    def set_name_book(self, new_name_book):
        self.name_book = new_name_book

    def get_name_book(self):
        return self.name_book


    def set_year_publication(self, new_year_publication):
        self.year_publication = new_year_publication

    def get_year_publication(self):
        return self.year_publication


    def set_publisher(self, new_publisher):
        self.publisher = new_publisher

    def get_publisher(self):
        return self.publisher


    def set_genre(self, new_genre):
        self.genre = new_genre

    def get_genre(self):
        return self.genre


    def set_author(self, new_author):
        self.author = new_author

    def get_author(self):
        return self.author


    def set_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price


book1 = Book("Майстер і Маргарита", 1967, "Видавництво Художня література", "Роман", "Михайло Булгаков", 250)
book1.display_info()

print("")

book2 = Book("1984", 1949, "Secker & Warburg", "Дистопія", "Джордж Орвелл", 180)
book2.display_info()

print("")

book1.set_price(300)
print("Нова ціна книги 'Майстер і Маргарита':", book1.get_price())

book1.get_price()
print("Ціна книги 'Майстер і Маргарита':", book1.get_price())
# Створіть базовий клас Employer з функцією Print()
# Фуукція має виводити інформацію про службовця.
# Для базового класу це може бути рядок із написом "This is Employer class".
# Створіть від нього три похідні класи: President, Manager, Worker
# Перевизначте функцію Print() для виведення інформації, що відповідає кожному типу службовця.

class Employer:
    def Print(self):
        print("This is Employer class")

class President(Employer):
    def Print(self):
        print("This is President class")

class Manager(Employer):
    def Print(self):
        print("This is Manager class")

class Worker(Employer):
    def Print(self):
        print("This is Worker class")

# Створення екземплярів кожного класу і виклик їх методу Print()

president = President()
president.Print()

manager = Manager()
manager.Print()

worker = Worker()
worker.Print()
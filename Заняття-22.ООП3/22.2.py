# Для класів із попереднього завдання реалізуйте магічний метод str,  а також метод int (який повертає вік службовця)

class Employer:
    def __str__(self):
        return "This is Employer class"

    def get_age(self):
        return 0


class President(Employer):
    def __str__(self):
        return "This is President class"

    def get_age(self):
        return 50


class Manager(Employer):
    def __str__(self):
        return "This is Manager class"

    def get_age(self):
        return 40


class Worker(Employer):
    def __str__(self):
        return "This is Worker class"

    def get_age(self):
        return 30


# Створення екземплярів кожного класу і виклик їх методів

president = President()
print(str(president))
print(president.get_age())

manager = Manager()
print(str(manager))
print(manager.get_age())

worker = Worker()
print(str(worker))
print(worker.get_age())
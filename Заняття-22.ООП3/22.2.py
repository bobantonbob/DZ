# Для класів із попереднього завдання реалізуйте магічний метод str,  а також метод int (який повертає вік службовця)

class Employer:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "This is Employer class"

    def __int__(self):
        return self.age


class President(Employer):
    def __str__(self):
        return "This is President class"


class Manager(Employer):
    def __str__(self):
        return "This is Manager class"

class Worker(Employer):
    def __str__(self):
        return "This is Worker class"


# Створення екземплярів кожного класу і виклик їх методів

president = President(50)
print(str(president))
print(int(president))

manager = Manager(40)
print(str(manager))
print(int(manager))

worker = Worker(30)
print(str(worker))
print(int(worker))
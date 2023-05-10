
# Завдання 1
# Створіть клас Human, який міститиме інформацію про людину.
# За допомогою механізму успадкування реалізуйте
# клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка),
# клас Pilot (містить інформацію про льотчика).
# Кожен із класів має містити необхідні для роботи методи.

class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print("Я людина !!! ")

class Builder(Human):
    def __init__(self, name, gender, specialization):
        super().__init__(name, gender)
        self.specialization = specialization

    def build(self):
        print("Я майстек на всі .....")


class Sailor(Human):
    def __init__(self, name, gender, experience):
        super().__init__(name, gender)
        self.experience = experience

    def sail(self):
        print("Я моряк, не бачу суші (")


class Pilot(Human):
    def __init__(self, name, gender, license):
        super().__init__(name, gender)
        self.license = license

    def fly(self):
        print("Я пілот, дивлюсь з гори !!!")


human = Human("Боб", 27)
human.speak()

builder = Builder("Рамшан", 47, "Разнорабочий")
builder.speak()
builder.build()

sailor = Sailor("Алита", 41, "11 років")
sailor.speak()
sailor.sail()

pilot = Pilot("Хан", 55, "Вантажна")
pilot.speak()
pilot.fly()
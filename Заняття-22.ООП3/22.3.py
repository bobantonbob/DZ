# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# на основі приклада опишить в класі методи: додавання, віднімання, ділення

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")


print(MathUtils.add(5, 3))
print(MathUtils.subtract(10, 4))
print(MathUtils.divide(12, 3))

try:
    print(MathUtils.divide(8, 0))
except ValueError as e:
    print(str(e))
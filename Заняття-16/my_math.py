def factorial(n):

    """
    Обчислює факторіал числа n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def ceil(x):
    """
    Повертає найменше ціле число, яке більше або дорівнює x.
    """
    return int(-(-x // 1))

def floor(x):
    """
    Повертає найбільше ціле число, яке менше або дорівнює x.
    """
    return int(x // 1)
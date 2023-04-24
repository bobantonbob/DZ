def max_num(numbers):

    """
    Знаходить максимальне число у списку чисел numbers.
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def sum_nums(numbers):
    """
    Обчислює суму чисел у списку numbers.
    """
    return sum(numbers)
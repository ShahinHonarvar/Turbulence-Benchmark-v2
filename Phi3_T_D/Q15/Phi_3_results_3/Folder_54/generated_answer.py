def sum_odd_ints_inclusive(numbers):
    return sum((number for index, number in enumerate(numbers[34:56]) if number % 2 != 0))
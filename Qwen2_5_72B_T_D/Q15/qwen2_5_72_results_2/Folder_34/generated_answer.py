def sum_odd_ints_inclusive(numbers):
    return sum((number for number in numbers[60:201] if number % 2 != 0))
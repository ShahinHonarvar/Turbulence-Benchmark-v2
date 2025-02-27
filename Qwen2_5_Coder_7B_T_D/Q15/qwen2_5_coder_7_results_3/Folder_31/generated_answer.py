import random

def sum_odd_ints_inclusive(numbers):
    return sum((n for n in numbers[75:89] if n % 2 == 1))
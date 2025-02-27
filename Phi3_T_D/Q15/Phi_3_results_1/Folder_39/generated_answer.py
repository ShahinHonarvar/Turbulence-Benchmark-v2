def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers[20:31]) if x % 2 != 0))
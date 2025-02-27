def sum_odd_ints_inclusive(numbers):
    return sum((x for x in numbers[80:201] if x % 2 != 0))
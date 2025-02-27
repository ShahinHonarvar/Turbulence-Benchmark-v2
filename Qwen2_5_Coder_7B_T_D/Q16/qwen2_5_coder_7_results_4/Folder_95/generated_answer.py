def sum_even_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers, 1) if 82 <= i <= 86 and x % 2 == 0))
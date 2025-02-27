def sum_even_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers[70:85]) if x % 2 == 0))
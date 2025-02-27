def sum_even_ints_inclusive(ints):
    return sum((x for i, x in enumerate(ints) if 13 <= i <= 68 and x % 2 == 0))
def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 6 <= i <= 8 and x % 2 == 0))
def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 22 <= i <= 63 and x % 2 == 0))
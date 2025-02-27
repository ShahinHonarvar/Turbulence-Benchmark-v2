def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 12 <= i <= 92 and x % 2 == 0))
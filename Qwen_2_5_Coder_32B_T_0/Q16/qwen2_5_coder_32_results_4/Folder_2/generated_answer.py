def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 15 <= i <= 39 and x % 2 == 0))
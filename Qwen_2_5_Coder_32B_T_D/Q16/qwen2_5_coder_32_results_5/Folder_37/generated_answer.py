def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 1 <= i <= 5 and x % 2 == 0))
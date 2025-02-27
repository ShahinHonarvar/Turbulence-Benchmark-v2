def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[22:89]) if x % 2 == 0))
def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 14 and i <= 64 and (x % 2 == 0)))
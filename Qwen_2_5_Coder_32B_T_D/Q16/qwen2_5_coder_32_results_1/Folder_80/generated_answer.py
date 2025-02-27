def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 64 and i <= 66 and (x % 2 == 0)))
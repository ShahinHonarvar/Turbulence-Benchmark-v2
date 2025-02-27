def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 91 and i <= 99 and (x % 2 == 0)))
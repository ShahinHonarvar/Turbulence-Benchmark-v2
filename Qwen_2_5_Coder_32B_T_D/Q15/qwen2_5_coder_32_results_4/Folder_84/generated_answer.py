def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 43 and i <= 86 and (x % 2 != 0)))
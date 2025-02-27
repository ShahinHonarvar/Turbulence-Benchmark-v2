def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 4 and i <= 8 and (x % 2 != 0)))
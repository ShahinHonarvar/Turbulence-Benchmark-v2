def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 22 and i <= 63 and (x % 2 != 0)))
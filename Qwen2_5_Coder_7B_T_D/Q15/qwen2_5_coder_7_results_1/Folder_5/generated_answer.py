def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i in (8, 9) and x % 2 != 0))
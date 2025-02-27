def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 310 <= i <= 370 and x % 2 != 0))
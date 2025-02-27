def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 62 <= i <= 78 and x % 2 != 0))
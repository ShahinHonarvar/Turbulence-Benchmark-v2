def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 62 <= i <= 99 and x % 2))
def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 14 <= i <= 64 and x % 2 != 0))
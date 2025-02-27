def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 36 <= i <= 46 and x % 2 != 0))
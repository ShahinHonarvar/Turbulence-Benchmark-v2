def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 20 <= i <= 30 and x % 2 != 0))
def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 10 <= i <= 66 and x % 2 != 0))
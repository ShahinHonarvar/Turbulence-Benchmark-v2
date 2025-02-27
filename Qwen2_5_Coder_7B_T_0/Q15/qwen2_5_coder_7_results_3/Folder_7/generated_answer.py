def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 661 <= i <= 924 and x % 2 != 0))
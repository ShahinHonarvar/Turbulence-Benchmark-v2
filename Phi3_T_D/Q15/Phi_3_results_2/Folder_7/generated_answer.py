def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst) if 661 <= idx <= 924 and val % 2 != 0))
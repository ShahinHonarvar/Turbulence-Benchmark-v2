def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[82:87]) if x % 2 != 0))
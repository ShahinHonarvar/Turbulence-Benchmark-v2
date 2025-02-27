def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i in range(661, 925) and x % 2 != 0))
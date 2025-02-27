def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 75 and i <= 85 and (x % 2 != 0)))
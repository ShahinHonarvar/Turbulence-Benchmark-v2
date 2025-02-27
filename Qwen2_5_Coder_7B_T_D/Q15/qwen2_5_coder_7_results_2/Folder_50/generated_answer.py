def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 70 and i <= 84 and (x % 2 != 0)))
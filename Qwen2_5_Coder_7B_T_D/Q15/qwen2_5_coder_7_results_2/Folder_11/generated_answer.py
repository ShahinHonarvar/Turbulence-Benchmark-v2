def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 37 and i <= 51 and (x % 2 != 0)))
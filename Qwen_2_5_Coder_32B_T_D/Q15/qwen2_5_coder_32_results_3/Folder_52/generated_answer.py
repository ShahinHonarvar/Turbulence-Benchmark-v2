def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 28 and i <= 38 and (x % 2 != 0))) if len(lst) > 38 else 0
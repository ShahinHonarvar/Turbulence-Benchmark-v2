def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 34 and i <= 55 and (x % 2 != 0))) if len(lst) > 55 else 0
def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 32 and i <= 35 and (x % 2 != 0))) if len(lst) > 35 else 0
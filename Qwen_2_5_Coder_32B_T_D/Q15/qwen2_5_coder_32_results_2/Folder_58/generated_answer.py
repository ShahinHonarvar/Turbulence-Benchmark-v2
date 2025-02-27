def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 209 and i <= 556 and (x % 2 != 0))) if len(lst) > 556 else 0
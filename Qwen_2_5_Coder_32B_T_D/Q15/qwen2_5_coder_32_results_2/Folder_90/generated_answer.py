def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 262 and i <= 746 and (x % 2 != 0))) if len(lst) > 746 else 0
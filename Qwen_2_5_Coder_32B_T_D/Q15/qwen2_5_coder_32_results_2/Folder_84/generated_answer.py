def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 43 <= i <= 86 and x % 2 != 0)) if len(lst) > 86 else 0
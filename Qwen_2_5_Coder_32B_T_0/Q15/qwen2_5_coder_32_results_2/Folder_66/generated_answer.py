def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 50 <= i <= 54 and x % 2 != 0)) if len(lst) > 54 else 0
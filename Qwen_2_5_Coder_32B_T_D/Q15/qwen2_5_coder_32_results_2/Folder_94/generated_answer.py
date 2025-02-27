def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 28 <= i <= 40 and x % 2 != 0)) if len(lst) > 40 else 0
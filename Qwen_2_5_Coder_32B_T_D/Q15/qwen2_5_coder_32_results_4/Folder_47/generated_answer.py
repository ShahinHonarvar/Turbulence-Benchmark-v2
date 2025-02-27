def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 37 <= i <= 76 and x % 2 != 0)) if len(lst) > 76 else 0
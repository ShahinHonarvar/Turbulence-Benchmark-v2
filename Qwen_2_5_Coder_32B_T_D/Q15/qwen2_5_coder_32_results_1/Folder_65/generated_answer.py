def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 56 <= i <= 98 and x % 2 != 0)) if len(lst) > 98 else 0
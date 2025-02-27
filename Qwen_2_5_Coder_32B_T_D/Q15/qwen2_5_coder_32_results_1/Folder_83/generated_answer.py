def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 90 <= i <= 200 and x % 2 != 0)) if len(lst) > 90 else 0
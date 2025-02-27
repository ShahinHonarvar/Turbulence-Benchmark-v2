def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 25 <= i <= 59 and x % 2 != 0)) if len(lst) > 59 else 0
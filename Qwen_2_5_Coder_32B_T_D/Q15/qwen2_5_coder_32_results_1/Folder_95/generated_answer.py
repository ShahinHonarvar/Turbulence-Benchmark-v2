def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 82 <= i <= 86 and x % 2 == 1)) if len(lst) > 86 else 0
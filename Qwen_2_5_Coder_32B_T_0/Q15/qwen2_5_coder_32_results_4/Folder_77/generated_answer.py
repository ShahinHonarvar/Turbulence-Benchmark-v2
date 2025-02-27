def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 527 <= i <= 538 and x % 2 != 0)) if len(lst) > 538 else 0
def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 80 <= i <= 200 and x % 2 != 0)) if len(lst) > 200 else 0
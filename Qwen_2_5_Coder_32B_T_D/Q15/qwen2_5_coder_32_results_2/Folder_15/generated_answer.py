def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[:4] if x % 2 != 0)) if len(lst) > 0 else 0
def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[33:37] if x % 2 != 0)) if len(lst) > 36 else 0
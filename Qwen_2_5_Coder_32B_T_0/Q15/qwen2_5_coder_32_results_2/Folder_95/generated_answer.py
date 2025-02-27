def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[82:87] if x % 2 != 0)) if len(lst) > 86 else 0
def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[32:36] if x % 2 != 0)) if len(lst) > 35 else 0
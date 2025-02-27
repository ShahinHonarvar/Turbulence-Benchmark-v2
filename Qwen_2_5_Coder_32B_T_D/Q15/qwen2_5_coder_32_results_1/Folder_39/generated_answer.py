def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[20:31] if x % 2 != 0)) if len(lst) > 30 else 0
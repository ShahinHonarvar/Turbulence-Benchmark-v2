def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[28:41] if x % 2 != 0)) if len(lst) > 40 else 0
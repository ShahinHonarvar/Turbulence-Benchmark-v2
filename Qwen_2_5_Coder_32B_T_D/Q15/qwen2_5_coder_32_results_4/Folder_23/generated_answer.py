def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[52:72] if x % 2 == 1)) if len(lst) > 71 else 0
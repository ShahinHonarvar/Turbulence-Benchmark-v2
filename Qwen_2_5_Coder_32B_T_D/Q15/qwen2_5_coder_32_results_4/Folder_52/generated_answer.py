def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[28:39] if x % 2 == 1)) if len(lst) > 38 else 0
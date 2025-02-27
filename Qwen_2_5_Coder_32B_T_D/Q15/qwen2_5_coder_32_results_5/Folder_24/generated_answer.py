def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[74:96] if x % 2 != 0)) if len(lst) > 95 else 0
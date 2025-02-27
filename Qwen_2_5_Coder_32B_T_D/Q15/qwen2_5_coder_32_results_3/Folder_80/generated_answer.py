def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[64:67] if x % 2 == 1)) if len(lst) > 66 else 0
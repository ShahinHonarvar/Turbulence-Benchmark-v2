def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[35:50] if x % 2 != 0)) if len(lst) > 49 else 0
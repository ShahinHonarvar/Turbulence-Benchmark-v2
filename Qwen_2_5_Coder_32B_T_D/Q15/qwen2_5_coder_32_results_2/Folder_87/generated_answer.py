def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[36:47] if x % 2 == 1)) if len(lst) > 46 else 0
def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[29:80] if x % 2 != 0)) if len(lst) > 79 else 0
def sum_odd_ints_inclusive(lst):
    if len(lst) < 36:
        return 0
    return sum((x for x in lst[32:36] if x % 2 != 0))
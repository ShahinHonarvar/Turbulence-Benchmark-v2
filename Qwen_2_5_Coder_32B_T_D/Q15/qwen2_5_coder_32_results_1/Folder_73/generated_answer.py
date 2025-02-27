def sum_odd_ints_inclusive(lst):
    if len(lst) < 93:
        return 0
    return sum((x for x in lst[19:93] if x % 2 != 0))
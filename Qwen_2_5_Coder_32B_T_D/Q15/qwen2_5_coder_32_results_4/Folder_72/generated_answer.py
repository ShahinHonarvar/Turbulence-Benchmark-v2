def sum_odd_ints_inclusive(lst):
    if len(lst) < 52:
        return 0
    return sum((x for x in lst[29:52] if x % 2 != 0))
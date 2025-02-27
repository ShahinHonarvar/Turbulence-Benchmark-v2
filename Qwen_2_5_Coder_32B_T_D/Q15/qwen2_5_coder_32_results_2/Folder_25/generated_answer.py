def sum_odd_ints_inclusive(lst):
    if len(lst) < 94:
        return 0
    return sum((x for x in lst[29:94] if x % 2 != 0))
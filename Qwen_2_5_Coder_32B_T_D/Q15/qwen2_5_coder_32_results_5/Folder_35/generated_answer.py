def sum_odd_ints_inclusive(lst):
    if len(lst) < 49:
        return 0
    return sum((x for x in lst[30:49] if x % 2 != 0))
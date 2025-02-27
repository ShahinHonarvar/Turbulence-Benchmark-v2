def sum_odd_ints_inclusive(lst):
    if 40 < len(lst) > 41:
        return sum((x for x in lst[40:42] if x % 2 != 0))
    return 0
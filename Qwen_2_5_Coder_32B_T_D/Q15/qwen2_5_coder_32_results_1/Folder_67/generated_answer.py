def sum_odd_ints_inclusive(lst):
    if len(lst) < 51:
        return 0
    return sum((x for x in lst[22:51] if x % 2 != 0))
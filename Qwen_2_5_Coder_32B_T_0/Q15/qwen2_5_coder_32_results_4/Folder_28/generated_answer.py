def sum_odd_ints_inclusive(lst):
    if len(lst) < 64:
        return 0
    return sum((x for x in lst[62:64] if x % 2 != 0))
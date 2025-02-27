def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[62:64] if x % 2 != 0)) if 63 < len(lst) else 0
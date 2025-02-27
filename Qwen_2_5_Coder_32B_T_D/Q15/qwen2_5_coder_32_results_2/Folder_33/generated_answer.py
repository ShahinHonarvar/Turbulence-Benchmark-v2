def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[667:775] if x % 2 != 0)) if 667 < len(lst) else 0
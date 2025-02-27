def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[56:58] if x % 2 != 0)) if len(lst) > 57 else 0
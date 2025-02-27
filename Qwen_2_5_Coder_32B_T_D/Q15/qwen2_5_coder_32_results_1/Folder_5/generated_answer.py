def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[8:10] if x % 2 != 0)) if len(lst) > 9 else 0
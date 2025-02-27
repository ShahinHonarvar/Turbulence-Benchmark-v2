def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[5:8] if x % 2 != 0)) if len(lst) > 7 else sum((x for x in lst[5:] if x % 2 != 0))
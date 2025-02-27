def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[1:6] if x % 2 != 0)) if len(lst) > 5 else sum((x for x in lst[1:] if x % 2 != 0))
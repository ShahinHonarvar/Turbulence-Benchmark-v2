def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[:5] if x % 2 != 0)) if len(lst) >= 5 else sum((x for x in lst if x % 2 != 0))
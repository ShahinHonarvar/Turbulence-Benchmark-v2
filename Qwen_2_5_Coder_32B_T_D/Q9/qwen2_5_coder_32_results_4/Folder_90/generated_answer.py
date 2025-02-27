def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 262 and i <= 746 and (x % 2 != 0)]
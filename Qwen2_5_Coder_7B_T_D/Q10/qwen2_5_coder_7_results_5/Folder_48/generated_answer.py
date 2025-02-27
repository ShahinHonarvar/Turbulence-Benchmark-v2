def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 385 and i < 999 and (x % 2 != 0)]
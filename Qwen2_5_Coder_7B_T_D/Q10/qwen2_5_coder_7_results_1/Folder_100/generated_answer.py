def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 22 and i < 24 and (x % 2 != 0)]
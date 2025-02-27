def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 13 and i < 66 and (x % 2 != 0)]
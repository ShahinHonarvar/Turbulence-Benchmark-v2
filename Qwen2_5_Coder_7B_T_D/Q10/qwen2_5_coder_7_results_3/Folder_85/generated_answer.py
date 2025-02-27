def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 4 and i < 6 and (x % 2 != 0)]
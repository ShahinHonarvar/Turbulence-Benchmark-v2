def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 28 and i < 53 and (x % 2 != 0)]
def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 38 and i < 81 and (x % 2 != 0)]
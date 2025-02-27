def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 295 and i < 573 and (x % 2 != 0)]
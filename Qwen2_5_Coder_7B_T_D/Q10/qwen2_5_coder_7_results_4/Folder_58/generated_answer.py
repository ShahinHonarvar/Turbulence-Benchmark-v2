def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 276 and i < 376 and (x % 2 != 0)]
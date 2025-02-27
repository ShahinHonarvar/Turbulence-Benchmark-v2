def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 369 and i < 983 and (x % 2 != 0)]
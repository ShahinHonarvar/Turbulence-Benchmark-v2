def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 19 < i < 94 and x % 2 != 0]
def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 3 < i < 8 and x % 2 != 0]
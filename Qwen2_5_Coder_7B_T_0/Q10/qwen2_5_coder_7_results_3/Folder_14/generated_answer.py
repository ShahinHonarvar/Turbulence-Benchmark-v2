def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 1 < i < 7 and x % 2 != 0]
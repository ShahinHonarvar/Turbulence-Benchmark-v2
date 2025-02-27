def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 49 < i < 74 and x % 2 != 0]
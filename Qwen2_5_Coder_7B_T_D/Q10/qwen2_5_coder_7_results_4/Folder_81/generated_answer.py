def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 10 < i < 11 and x % 2 != 0]
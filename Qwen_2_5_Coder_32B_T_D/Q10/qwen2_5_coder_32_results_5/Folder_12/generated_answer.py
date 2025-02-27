def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 23 < i < 45 and x % 2 != 0]
def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 13 < i < 70 and x % 2 != 0]
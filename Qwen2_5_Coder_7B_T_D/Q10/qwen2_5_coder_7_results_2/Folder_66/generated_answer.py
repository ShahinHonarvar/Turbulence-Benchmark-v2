def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 13 < i < 76 and x % 2 != 0]
def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 15 < i < 100 and x % 2 != 0]
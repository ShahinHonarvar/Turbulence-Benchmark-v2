def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 30 < i < 200 and x % 2 != 0]
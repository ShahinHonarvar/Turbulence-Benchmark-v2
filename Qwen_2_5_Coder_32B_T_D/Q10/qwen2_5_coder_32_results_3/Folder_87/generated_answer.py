def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 32 < i < 99 and x % 2 == 1]
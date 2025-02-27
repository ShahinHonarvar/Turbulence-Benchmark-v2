def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 100 and i < 101 and (x % 2 != 0)]
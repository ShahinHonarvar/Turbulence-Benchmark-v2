def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 43 and i < 99 and (x % 2 != 0)]
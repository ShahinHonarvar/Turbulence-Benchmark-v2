def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 49 and i < 74 and (x % 2 == 1)]
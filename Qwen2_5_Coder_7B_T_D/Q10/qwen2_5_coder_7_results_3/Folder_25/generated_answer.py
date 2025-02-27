def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 41 and i < 69 and (x % 2 != 0)]
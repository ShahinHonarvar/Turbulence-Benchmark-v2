def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 64 and i < 80 and (x % 2 != 0)]
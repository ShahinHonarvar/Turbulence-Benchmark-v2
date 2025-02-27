def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 18 and i < 37 and (x % 2 != 0)]
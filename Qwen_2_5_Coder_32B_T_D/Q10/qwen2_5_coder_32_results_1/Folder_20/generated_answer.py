def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 59 and i < 93 and (x % 2 != 0)]
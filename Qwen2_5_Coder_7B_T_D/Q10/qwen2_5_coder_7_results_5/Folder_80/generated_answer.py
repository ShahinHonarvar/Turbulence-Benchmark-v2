def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 69 and i < 97 and (x % 2 != 0)]
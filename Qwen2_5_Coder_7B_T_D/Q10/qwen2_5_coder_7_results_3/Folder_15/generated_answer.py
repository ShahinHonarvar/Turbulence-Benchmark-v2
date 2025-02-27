def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[:4]) if i != 0 and i != 3 and (x % 2 != 0)]
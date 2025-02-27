def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 3 and i < 8 and (x % 2 == 1)]
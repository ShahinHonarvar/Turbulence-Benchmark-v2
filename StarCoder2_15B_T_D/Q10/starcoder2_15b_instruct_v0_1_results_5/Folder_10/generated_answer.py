def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 48 and i < 74 and (x % 2 == 1)]
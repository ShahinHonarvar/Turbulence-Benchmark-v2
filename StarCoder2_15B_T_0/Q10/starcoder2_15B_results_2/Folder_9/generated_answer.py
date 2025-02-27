def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 70 and i < 72 and (x % 2 == 1)]
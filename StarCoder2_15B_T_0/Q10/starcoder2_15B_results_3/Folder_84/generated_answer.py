def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 50 and i < 92 and (x % 2 == 1)]
def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 19 < i < 94 and x % 2 == 1]
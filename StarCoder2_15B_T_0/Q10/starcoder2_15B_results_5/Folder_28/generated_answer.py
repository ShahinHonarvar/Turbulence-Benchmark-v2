def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 20 < i < 51 and x % 2 == 1]
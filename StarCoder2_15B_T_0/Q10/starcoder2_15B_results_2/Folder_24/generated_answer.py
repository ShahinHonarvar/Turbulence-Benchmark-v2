def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 13 <= i < 66 and x % 2 == 1]
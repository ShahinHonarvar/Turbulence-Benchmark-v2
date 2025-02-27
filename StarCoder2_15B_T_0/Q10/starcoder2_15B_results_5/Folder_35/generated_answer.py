def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 10 <= i < 79 and x % 2 == 1]
def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 18 < i < 60 and x % 2 == 1]
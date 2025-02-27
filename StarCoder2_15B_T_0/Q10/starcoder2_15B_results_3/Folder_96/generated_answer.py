def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 50 < i < 200 and x % 2 == 1]
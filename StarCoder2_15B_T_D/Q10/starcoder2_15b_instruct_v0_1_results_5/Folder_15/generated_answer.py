def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i % 2 == 1 and 0 < i < 3]
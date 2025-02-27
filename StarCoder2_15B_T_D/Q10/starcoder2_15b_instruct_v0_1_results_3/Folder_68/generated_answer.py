def all_odd_ints_exclusive(ints):
    return [int for i, int in enumerate(ints) if i % 2 == 1 and 0 < i < 8]
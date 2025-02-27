def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if 1 <= i <= 5 and x % 2 != 0]
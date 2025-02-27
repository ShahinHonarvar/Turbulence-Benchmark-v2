def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 6 and i <= 8 and (x % 2 == 1)]
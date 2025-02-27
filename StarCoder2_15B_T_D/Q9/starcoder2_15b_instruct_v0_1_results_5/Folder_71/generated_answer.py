def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 26 and i <= 52 and (x % 2 != 0)]
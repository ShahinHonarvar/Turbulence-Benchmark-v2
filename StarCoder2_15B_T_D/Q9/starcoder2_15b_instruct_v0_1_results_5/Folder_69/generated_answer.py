def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 32 and i <= 35 and (x % 2 == 1)]
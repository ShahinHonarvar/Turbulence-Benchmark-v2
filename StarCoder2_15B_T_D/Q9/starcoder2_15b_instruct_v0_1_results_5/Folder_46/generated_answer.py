def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 30 and i <= 87 and (x % 2 == 1)]
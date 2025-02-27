def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 15 and i <= 39 and (x % 2 == 1)]
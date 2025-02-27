def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 37 and i <= 51 and (x % 2 == 1)]
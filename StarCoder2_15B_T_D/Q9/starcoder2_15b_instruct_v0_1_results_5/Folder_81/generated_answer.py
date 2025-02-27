def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 10 and i <= 100 and (x % 2 == 1)]
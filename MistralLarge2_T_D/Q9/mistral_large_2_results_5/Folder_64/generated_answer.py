def all_odd_ints_inclusive(ints):
    return [i for idx, i in enumerate(ints) if idx in range(5) and i % 2 != 0]
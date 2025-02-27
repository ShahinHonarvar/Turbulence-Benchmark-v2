def all_odd_ints_inclusive(ints):
    if len(ints) < 82:
        return []
    return [i for i in ints[56:83] if i % 2 == 1]
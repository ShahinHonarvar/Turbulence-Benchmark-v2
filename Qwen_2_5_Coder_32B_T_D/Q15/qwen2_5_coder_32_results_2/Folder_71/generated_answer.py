def sum_odd_ints_inclusive(ints):
    if len(ints) < 53:
        return 0
    return sum((x for x in ints[26:53] if x % 2 != 0))
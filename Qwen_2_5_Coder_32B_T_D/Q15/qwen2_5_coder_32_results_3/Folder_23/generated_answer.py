def sum_odd_ints_inclusive(ints):
    if len(ints) < 72:
        return 0
    return sum((x for x in ints[52:72] if x % 2 != 0))
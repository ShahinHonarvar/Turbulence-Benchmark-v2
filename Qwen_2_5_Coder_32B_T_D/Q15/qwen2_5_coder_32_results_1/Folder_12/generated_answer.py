def sum_odd_ints_inclusive(ints):
    return sum((x for i, x in enumerate(ints) if 14 <= i <= 64 and x % 2 != 0)) if len(ints) > 64 else 0
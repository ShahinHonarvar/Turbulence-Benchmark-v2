def sum_odd_ints_inclusive(ints):
    return sum((x for i, x in enumerate(ints) if 22 <= i <= 50 and x % 2 != 0))
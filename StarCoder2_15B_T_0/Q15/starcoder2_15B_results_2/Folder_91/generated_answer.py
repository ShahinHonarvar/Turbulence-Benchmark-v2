def sum_odd_ints_inclusive(ints):
    return sum((i for i in ints[0:6] if i % 2 != 0))
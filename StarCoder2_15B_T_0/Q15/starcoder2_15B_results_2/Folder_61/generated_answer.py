def sum_odd_ints_inclusive(ints):
    return sum((i for i in ints[0:8] if i % 2 != 0))
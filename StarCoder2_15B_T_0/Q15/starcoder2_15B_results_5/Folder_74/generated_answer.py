def sum_odd_ints_inclusive(ints):
    return sum((i for i in ints[17:80] if i % 2 != 0))
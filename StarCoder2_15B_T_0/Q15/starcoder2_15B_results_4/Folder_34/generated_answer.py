def sum_odd_ints_inclusive(ints):
    return sum((i for i in ints[60:201] if i % 2 != 0))
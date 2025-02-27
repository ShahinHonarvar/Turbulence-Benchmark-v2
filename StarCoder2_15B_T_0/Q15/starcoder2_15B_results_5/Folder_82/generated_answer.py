def sum_odd_ints_inclusive(ints):
    return sum((i for i in ints[20:201] if i % 2 != 0))
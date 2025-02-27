def sum_odd_ints_inclusive(ints):
    return sum(filter(lambda x: x % 2 == 1, ints[21:98]))
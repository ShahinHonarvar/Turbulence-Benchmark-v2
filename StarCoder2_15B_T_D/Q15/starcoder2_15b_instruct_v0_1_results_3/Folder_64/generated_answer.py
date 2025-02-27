def sum_odd_ints_inclusive(ints):
    return sum((odd for odd in ints[0:5] if odd % 2 == 1))
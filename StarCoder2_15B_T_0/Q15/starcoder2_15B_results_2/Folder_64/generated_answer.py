def sum_odd_ints_inclusive(ints):
    return sum((int for int in ints[0:5] if int % 2 != 0))